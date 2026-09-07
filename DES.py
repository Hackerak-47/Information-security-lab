# des.py
# DES Encryption / Decryption
# Supports: ECB, CBC, CFB, OFB, OPENPGP
#
# Install:
# pip install pycryptodome

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


BLOCK_SIZE = 8


def get_key():
    while True:
        key = input("Enter DES key (exactly 8 characters): ")

        if len(key) == 8:
            return key.encode()

        print("ERROR: DES key must be exactly 8 characters.")


def choose_mode():
    print("\nDES MODES")
    print("1. ECB")
    print("2. CBC")
    print("3. CFB")
    print("4. OFB")
    print("5. OPENPGP")

    while True:
        choice = input("Enter mode: ")

        if choice in ["1", "2", "3", "4", "5"]:
            return choice

        print("Invalid choice.")


def encrypt_des(plaintext, key, mode_choice):
    data = plaintext.encode()

    # ---------------- ECB ----------------
    if mode_choice == "1":
        cipher = DES.new(key, DES.MODE_ECB)

        padded = pad(data, BLOCK_SIZE)
        ciphertext = cipher.encrypt(padded)

        return {
            "mode": "ECB",
            "iv": None,
            "ciphertext": base64.b64encode(ciphertext).decode()
        }

    # ---------------- CBC ----------------
    elif mode_choice == "2":
        iv = get_random_bytes(BLOCK_SIZE)

        cipher = DES.new(
            key,
            DES.MODE_CBC,
            iv=iv
        )

        padded = pad(data, BLOCK_SIZE)
        ciphertext = cipher.encrypt(padded)

        return {
            "mode": "CBC",
            "iv": base64.b64encode(iv).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode()
        }

    # ---------------- CFB ----------------
    elif mode_choice == "3":
        iv = get_random_bytes(BLOCK_SIZE)

        cipher = DES.new(
            key,
            DES.MODE_CFB,
            iv=iv
        )

        ciphertext = cipher.encrypt(data)

        return {
            "mode": "CFB",
            "iv": base64.b64encode(iv).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode()
        }

    # ---------------- OFB ----------------
    elif mode_choice == "4":
        iv = get_random_bytes(BLOCK_SIZE)

        cipher = DES.new(
            key,
            DES.MODE_OFB,
            iv=iv
        )

        ciphertext = cipher.encrypt(data)

        return {
            "mode": "OFB",
            "iv": base64.b64encode(iv).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode()
        }

    # ---------------- OPENPGP ----------------
    elif mode_choice == "5":
        cipher = DES.new(
            key,
            DES.MODE_OPENPGP
        )

        ciphertext = cipher.encrypt(data)

        return {
            "mode": "OPENPGP",
            "iv": base64.b64encode(cipher.iv).decode(),
            "ciphertext": base64.b64encode(ciphertext).decode()
        }


def decrypt_des(ciphertext_b64, key, mode, iv_b64=None):
    ciphertext = base64.b64decode(ciphertext_b64)

    # ---------------- ECB ----------------
    if mode == "ECB":
        cipher = DES.new(
            key,
            DES.MODE_ECB
        )

        plaintext = cipher.decrypt(ciphertext)
        return unpad(plaintext, BLOCK_SIZE).decode()

    # ---------------- CBC ----------------
    elif mode == "CBC":
        iv = base64.b64decode(iv_b64)

        cipher = DES.new(
            key,
            DES.MODE_CBC,
            iv=iv
        )

        plaintext = cipher.decrypt(ciphertext)

        return unpad(plaintext, BLOCK_SIZE).decode()

    # ---------------- CFB ----------------
    elif mode == "CFB":
        iv = base64.b64decode(iv_b64)

        cipher = DES.new(
            key,
            DES.MODE_CFB,
            iv=iv
        )

        plaintext = cipher.decrypt(ciphertext)

        return plaintext.decode()

    # ---------------- OFB ----------------
    elif mode == "OFB":
        iv = base64.b64decode(iv_b64)

        cipher = DES.new(
            key,
            DES.MODE_OFB,
            iv=iv
        )

        plaintext = cipher.decrypt(ciphertext)

        return plaintext.decode()

    # ---------------- OPENPGP ----------------
    elif mode == "OPENPGP":
        encrypted_iv = base64.b64decode(iv_b64)

        cipher = DES.new(
            key,
            DES.MODE_OPENPGP,
            iv=encrypted_iv
        )

        plaintext = cipher.decrypt(ciphertext)

        return plaintext.decode()


def main():
    print("=" * 50)
    print("             DES ENCRYPTION")
    print("=" * 50)

    key = get_key()

    mode_choice = choose_mode()

    plaintext = input("\nEnter plaintext: ")

    try:
        result = encrypt_des(
            plaintext,
            key,
            mode_choice
        )

        print("\n========== ENCRYPTION ==========")
        print("Mode       :", result["mode"])
        print("IV         :", result["iv"])
        print("Ciphertext :", result["ciphertext"])

        print("\n========== DECRYPTION ==========")

        decrypted = decrypt_des(
            result["ciphertext"],
            key,
            result["mode"],
            result["iv"]
        )

        print("Plaintext  :", decrypted)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
