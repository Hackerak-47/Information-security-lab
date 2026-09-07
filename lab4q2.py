pip install cryptography sympy flask
# rabin_kms.py
#
# HealthCare Inc.
# Centralized Key Management Service using Rabin Cryptosystem
#
# Educational implementation
#
# Install:
# pip install flask cryptography sympy

from flask import Flask, request, jsonify
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from sympy import nextprime
import hashlib
import secrets
import json
import os
import logging
import time
from datetime import datetime, timedelta


app = Flask(__name__)

# ============================================================
# CONFIGURATION
# ============================================================

KEY_SIZE = 1024
RENEWAL_MONTHS = 12

DATABASE_FILE = "rabin_keys.json"
AUDIT_FILE = "rabin_audit.log"

# Master key used to encrypt private keys at rest.
# In a real system this must come from an HSM/KMS/environment
# secret and NOT be hard-coded.
MASTER_KEY_FILE = "kms_master.key"


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    filename=AUDIT_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def audit(operation, facility):
    logging.info(
        "OPERATION=%s | FACILITY=%s",
        operation,
        facility
    )


# ============================================================
# MASTER STORAGE KEY
# ============================================================

def get_master_key():

    if os.path.exists(MASTER_KEY_FILE):

        with open(MASTER_KEY_FILE, "rb") as f:
            return f.read()

    key = get_random_bytes(32)

    with open(MASTER_KEY_FILE, "wb") as f:
        f.write(key)

    return key


MASTER_KEY = get_master_key()


# ============================================================
# DATABASE
# ============================================================

def load_database():

    if not os.path.exists(DATABASE_FILE):
        return {}

    with open(DATABASE_FILE, "r") as f:
        return json.load(f)


def save_database(database):

    with open(DATABASE_FILE, "w") as f:
        json.dump(
            database,
            f,
            indent=4
        )


# ============================================================
# SECURE PRIVATE KEY STORAGE
# ============================================================

def encrypt_private_key(private_key):

    cipher = AES.new(
        MASTER_KEY,
        AES.MODE_GCM
    )

    ciphertext, tag = cipher.encrypt_and_digest(
        private_key.encode()
    )

    return {
        "nonce": cipher.nonce.hex(),
        "tag": tag.hex(),
        "ciphertext": ciphertext.hex()
    }


def decrypt_private_key(data):

    nonce = bytes.fromhex(data["nonce"])
    tag = bytes.fromhex(data["tag"])
    ciphertext = bytes.fromhex(data["ciphertext"])

    cipher = AES.new(
        MASTER_KEY,
        AES.MODE_GCM,
        nonce=nonce
    )

    plaintext = cipher.decrypt_and_verify(
        ciphertext,
        tag
    )

    return plaintext.decode()


# ============================================================
# RABIN KEY GENERATION
# ============================================================

def generate_rabin_keys(bits=1024):

    # Rabin requires p and q to be 3 mod 4
    # for simple square-root decryption.

    half = bits // 2

    while True:

        p = int(nextprime(
            secrets.randbits(half)
        ))

        if p % 4 == 3:
            break

    while True:

        q = int(nextprime(
            secrets.randbits(half)
        ))

        if q % 4 == 3 and q != p:
            break

    n = p * q

    public_key = {
        "n": n
    }

    private_key = {
        "p": p,
        "q": q
    }

    return public_key, private_key


# ============================================================
# REGISTER FACILITY
# ============================================================

def register_facility(facility_id):

    database = load_database()

    if facility_id in database:

        return False, "Facility already exists"

    public_key, private_key = generate_rabin_keys(
        KEY_SIZE
    )

    encrypted_private = encrypt_private_key(
        json.dumps(private_key)
    )

    database[facility_id] = {

        "public_key": public_key,

        "private_key": encrypted_private,

        "created":
            datetime.now().isoformat(),

        "expires":
            (
                datetime.now()
                + timedelta(
                    days=365
                )
            ).isoformat(),

        "revoked": False,

        "version": 1
    }

    save_database(database)

    audit(
        "KEY_GENERATION",
        facility_id
    )

    return True, database[facility_id]


# ============================================================
# DISTRIBUTE KEY
# ============================================================

def distribute_keys(facility_id):

    database = load_database()

    if facility_id not in database:

        return None, "Facility not found"

    facility = database[facility_id]

    if facility["revoked"]:

        audit(
            "DISTRIBUTION_DENIED_REVOKED",
            facility_id
        )

        return None, "Key is revoked"

    private_key = decrypt_private_key(
        facility["private_key"]
    )

    audit(
        "KEY_DISTRIBUTION",
        facility_id
    )

    return {

        "facility_id": facility_id,

        "public_key":
            facility["public_key"],

        "private_key":
            json.loads(private_key),

        "version":
            facility["version"]

    }, None


# ============================================================
# REVOKE KEY
# ============================================================

def revoke_key(facility_id):

    database = load_database()

    if facility_id not in database:

        return False, "Facility not found"

    database[facility_id]["revoked"] = True

    save_database(database)

    audit(
        "KEY_REVOCATION",
        facility_id
    )

    return True, "Key revoked successfully"


# ============================================================
# RENEW KEY
# ============================================================

def renew_key(facility_id):

    database = load_database()

    if facility_id not in database:

        return False, "Facility not found"

    public_key, private_key = generate_rabin_keys(
        KEY_SIZE
    )

    encrypted_private = encrypt_private_key(
        json.dumps(private_key)
    )

    old_version = database[facility_id]["version"]

    database[facility_id] = {

        "public_key": public_key,

        "private_key":
            encrypted_private,

        "created":
            datetime.now().isoformat(),

        "expires":
            (
                datetime.now()
                + timedelta(
                    days=365
                )
            ).isoformat(),

        "revoked": False,

        "version": old_version + 1
    }

    save_database(database)

    audit(
        "KEY_RENEWAL",
        facility_id
    )

    return True, "Key renewed successfully"


# ============================================================
# AUTOMATIC RENEWAL
# ============================================================

def automatic_renewal():

    database = load_database()

    for facility_id, facility in database.items():

        expiry = datetime.fromisoformat(
            facility["expires"]
        )

        if datetime.now() >= expiry:

            renew_key(
                facility_id
            )


# ============================================================
# FLASK API
# ============================================================

@app.route("/register", methods=["POST"])
def api_register():

    data = request.json

    facility_id = data.get(
        "facility_id"
    )

    if not facility_id:

        return jsonify({
            "error": "facility_id required"
        }), 400

    success, result = register_facility(
        facility_id
    )

    if not success:

        return jsonify({
            "error": result
        }), 400

    return jsonify({
        "message":
            "Facility registered",
        "facility":
            result
    })


@app.route("/keys/<facility_id>", methods=["GET"])
def api_keys(facility_id):

    result, error = distribute_keys(
        facility_id
    )

    if error:

        return jsonify({
            "error": error
        }), 404

    return jsonify(result)


@app.route("/revoke/<facility_id>", methods=["POST"])
def api_revoke(facility_id):

    success, message = revoke_key(
        facility_id
    )

    if not success:

        return jsonify({
            "error": message
        }), 404

    return jsonify({
        "message": message
    })


@app.route("/renew/<facility_id>", methods=["POST"])
def api_renew(facility_id):

    success, message = renew_key(
        facility_id
    )

    if not success:

        return jsonify({
            "error": message
        }), 404

    return jsonify({
        "message": message
    })


# ============================================================
# TRADE-OFF ANALYSIS
# ============================================================

def tradeoff_analysis():

    print("\n")
    print("=" * 70)
    print("RABIN vs RSA TRADE-OFF ANALYSIS")
    print("=" * 70)

    print("""
RABIN
----
1. Security is closely related to integer factorization.
2. Encryption operation is mathematically simple: c = m^2 mod n.
3. Decryption produces four possible square roots.
4. Additional padding/encoding is needed to identify the correct plaintext.
5. Efficient encryption.
6. Raw Rabin encryption should not be used directly in production.

RSA
---
1. Security also depends on difficulty of factoring n.
2. Supports encryption and digital signatures.
3. Uses modular exponentiation.
4. Standardized padding schemes such as OAEP and PSS are available.
5. More widely deployed than Rabin.
6. Better library and protocol support.

CONCLUSION
----------
Rabin has an elegant relationship with integer factorization,
but RSA is generally more practical because of its maturity,
standard padding schemes, signatures and ecosystem support.
""")


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print("HEALTHCARE INC. - RABIN KEY MANAGEMENT SERVICE")
    print("=" * 70)

    print("Key size:", KEY_SIZE, "bits")
    print("Renewal:", RENEWAL_MONTHS, "months")

    automatic_renewal()

    tradeoff_analysis()

    print("\nStarting API...")
    print("http://127.0.0.1:5000")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )
