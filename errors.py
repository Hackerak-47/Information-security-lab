# ---------------------------------------------------------
# 1. HASH FUNCTION
# ---------------------------------------------------------

def hash(message):
    hash_value = hashlib.sha256(message).hexdigest()
    return hash_value

# ❌ ERROR:
# You named your function "hash".
# It works, but "hash" is already a Python built-in function.
# Better name: my_hash() or sha256_hash()


# ---------------------------------------------------------
# 2. AES KEY
# ---------------------------------------------------------

def aes_key():
    key = get_random_bytes(AES.block_size)
    return key

# ✅ CORRECT
# AES.block_size = 16 bytes
# So this generates a valid 128-bit AES key.


# ---------------------------------------------------------
# 3. AES ENCRYPTION
# ---------------------------------------------------------

def aes_enc(text, key):
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(pad(text, AES.block_size))
    return ciphertext, iv

# ✅ CORRECT
# text must be bytes.
# IV = 16 bytes for AES-CBC.
# pad() is correct.


# ---------------------------------------------------------
# 4. AES DECRYPTION
# ---------------------------------------------------------

def aes_dec(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    text = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return text

# ✅ CORRECT
# Returns bytes.
# Therefore later:
# dec.decode()
# is correct.


# ---------------------------------------------------------
# 5. SIGNATURE
# ---------------------------------------------------------

def sign_message(private_key, message):
    signature = private_key.sign(
        message.encode(),
        padding.PKCS1v15(),
        hashes.SHA256()
    )
    return signature

# ✅ Works.
# You are signing the HASH STRING.
#
# For your lab this is acceptable.
# Don't change it unless your question specifically asks
# for signing a precomputed digest.


# ---------------------------------------------------------
# 6. VERIFY SIGNATURE
# ---------------------------------------------------------

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        print("Signature is valid")
        return 1

    except:
        print("Signature is invalid")
        return 0

# ✅ Logic is correct.


# ---------------------------------------------------------
# 7. WRITING PATIENT FILE
# ---------------------------------------------------------

with open("patient.txt", "a") as file:
    file.write("patient[id]")

# ❌❌ BIG ERROR
#
# This does NOT write the value of patient[id].
#
# You wrote:
#     "patient[id]"
#
# Because of quotes, Python writes literally:
#     patient[id]
#
# FIX:
file.write(str(patient[id]))


# ---------------------------------------------------------
# 8. ENCODING PATIENT DATA
# ---------------------------------------------------------

text, iv = aes_enc(str(patient[id]).encode(), k)

# ✅ This part is correct.
#
# patient[id] -> dictionary
# str(...)    -> string
# .encode()   -> bytes
# AES         -> ciphertext bytes


# ---------------------------------------------------------
# 9. AES CIPHERTEXT
# ---------------------------------------------------------

h = hash(text)

# ✅ CORRECT
#
# text is already encrypted bytes.
# DO NOT do:
#
# hash(text.encode())   ❌
#
# because ciphertext is already bytes.


# ---------------------------------------------------------
# 10. RSA KEY GENERATION
# ---------------------------------------------------------

private, public = generate_keys()

# ⚠️ LOGICAL ERROR
#
# You are generating a NEW RSA key pair every time
# a patient record is created.
#
# For MediSecure:
# Patient should have their own RSA key pair.
# Patient private key -> signing
# Patient public key  -> verification.
#
# Your current code stores the keys inside the record,
# which is not the intended design.


# ---------------------------------------------------------
# 11. TIMESTAMP
# ---------------------------------------------------------

time = time.time()

# ❌ ERROR
#
# You imported:
#     import time
#
# Then you created a variable called:
#     time
#
# After this line, "time" is no longer the module.
#
# FIX:
timestamp = time.time()


# ---------------------------------------------------------
# 12. RECORD
# ---------------------------------------------------------

record[id] = {
    "enc": text,
    "aes_key": k,
    "iv": iv,
    "sign": sign,
    "hash": h,
    "timestamp": timestamp,
    "public": public,
    "private": private
}

# ⚠️ PROBLEM
#
# You are storing the PRIVATE RSA KEY in the record.
#
# "private": private
#
# ❌ This is bad design for the hospital system.
#
# The private key should remain with the patient
# and should NOT be stored with the record.


# ---------------------------------------------------------
# 13. DISPLAY
# ---------------------------------------------------------

print("timsetamp", record[id]["timestamp"])

# ❌ "timsetamp" is only a spelling mistake in the output.
# It does NOT affect the program.
#
# Better:
print("timestamp", record[id]["timestamp"])


# ---------------------------------------------------------
# 14. VERIFICATION
# ---------------------------------------------------------

crypt = record[id]["enc"]

has = hash(crypt)

# ✅ CORRECT
#
# crypt is ciphertext bytes.
# Hash it directly.


# ---------------------------------------------------------
# 15. HASH COMPARISON
# ---------------------------------------------------------

if has == record[id]["hash"]:
    print("first stage verified")

# ✅ CORRECT
#
# This checks integrity:
#
# current ciphertext hash
#          vs
# stored ciphertext hash


# ---------------------------------------------------------
# 16. SIGNATURE VERIFICATION
# ---------------------------------------------------------

v = verify_signature(
    record[id]["public"],
    has,
    record[id]["sign"]
)

# ✅ Correct according to your signing method.
#
# You signed the original hash,
# so you verify the newly calculated hash.


# ---------------------------------------------------------
# 17. DECRYPTION
# ---------------------------------------------------------

dec = aes_dec(
    record[id]["enc"],
    record[id]["aes_key"],
    record[id]["iv"]
)

print("dec msg :", dec.decode())

# ✅ CORRECT
#
# AES decryption returns bytes.
# .decode() converts those bytes back to string.


# =========================================================
# MOST IMPORTANT ERRORS TO REMEMBER FOR EXAM
# =========================================================

# ❌ file.write("patient[id]")
#    writes literal text.
#
# ✅ file.write(str(patient[id]))


# ❌ time = time.time()
#    destroys the time module reference.
#
# ✅ timestamp = time.time()


# ❌ storing patient's private RSA key with the record
#    is a design/security mistake.
#
# ✅ keep private key separately.


# ⚠️ generating a new RSA key pair for every record
#    is not the intended patient-key design.
#
# ✅ patient gets one RSA key pair.


# ✅ ciphertext is already bytes.
#    Don't .encode() ciphertext.


# ✅ decrypted AES output is bytes.
#    .decode() after decryption is correct.


# ✅ AES key = 16/24/32 bytes
# ✅ AES block size = 16 bytes
# ✅ AES-CBC IV = 16 bytes


# ✅ DES key = 8 bytes
# ✅ DES block size = 8 bytes
# ✅ DES-CBC IV = 8 bytes
