# aes.py
# AES Encryption / Decryption
#
# Supports:
# AES-128
# AES-192
# AES-256
#
# Modes:
# ECB
# CBC
# CFB
# OFB
# CTR
# EAX
# GCM
# CCM
# SIV
#
# Install:
# pip install pycryptodome

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64


BLOCK_SIZE = 16


def get_key():
    print("\nAES KEY SIZES")
    print("1. AES-128 -> 16 characters")
    print("2. AES-192 -> 24 characters")
    print("3. AES-256 -> 32 characters")

    while True:
        choice = input("Choose key size: ")

        if choice == "1":
            size = 16
            break
        elif choice == "2":
            size = 24
            break
        elif choice == "3":
            size = 32
            break
        else:
            print("Invalid choice.")

    while True:
        key = input(f"Enter AES key ({size} characters): ")

        if len(key) == size:
            return key.encode()

        print(f"ERROR: Key must be exactly {size} characters.")


def choose_mode():
    print("\nAES MODES")
    print("1. ECB")
    print("2. CBC")
    print("3. CFB")
    print("4. OFB")
    print("5. CTR")
    print("6. EAX")
    print("7. GCM")
    print("8. CCM")
    print("9. SIV")

    while True:
        choice = input("Enter mode: ")

        if choice in [
            "1", "2", "3", "4", "5",
            "6", "7", "8", "9"
        ]:
            return choice

        print("Invalid choice.")


def encrypt_aes(plaintext, key, mode_choice):
    data = plaintext.encode()

    # ==================================================
    # ECB
    # ==================================================
    if mode_choice == "1":

        cipher = AES.new(
            key,
            AES.MODE_ECB
        )

        padded = pad(data, BLOCK_SIZE)

        ciphertext = cipher.encrypt(padded)

        return {
            "mode": "ECB",
            "iv": None,
            "nonce": None,
            "tag": None,
            "ciphertext":
                base64.b64encode(ciphertext).decode()
        }

    # ==================================================
    # CBC
    # ==================================================
    elif mode_choice == "2":

        iv = get_random_bytes(BLOCK_SIZE)

        cipher = AES.new(
            key,
            AES.MODE_CBC,
            iv=iv
        )

        padded = pad(data, BLOCK_SIZE)

        ciphertext = cipher.encrypt(padded)

        return {
            "mode": "CBC",
            "iv":
                base64.b64encode(iv).decode(),
            "nonce": None,
            "tag": None,
            "ciphertext":
                base64.b64encode(ciphertext).decode()
        }

    # ==================================================
    # CFB
    # ==================================================
    elif mode_choice == "3":

        iv = get_random_bytes(BLOCK_SIZE)

        cipher = AES.new(
            key,
            AES.MODE_CFB,
            iv=iv
        )

        ciphertext = cipher.encrypt(data)

        return {
            "mode": "CFB",
            "iv":
                base64.b64encode(iv).decode(),
            "nonce": None,
            "tag": None,
            "ciphertext":
                base64.b64encode(ciphertext).decode()
        }

    # ==================================================
    # OFB
    # ==================================================
    elif mode_choice == "4":

        iv = get_random_bytes(BLOCK_SIZE)

        cipher = AES.new(
            key,
            AES.MODE_OFB,
            iv=iv
        )

        ciphertext = cipher.encrypt(data)

        return {
            "mode": "OFB",
            "iv":
                base64.b64encode(iv).decode(),
            "nonce": None,
            "tag": None,
            "ciphertext":
                base64.b64encode(ciphertext).decode()
        }

    # ==================================================
    # CTR
    # ==================================================
    elif mode_choice == "5":

        nonce = get_random_bytes(8)

        cipher = AES.new(
            key,
            AES.MODE_CTR,
            nonce=nonce
        )

        ciphertext = cipher.encrypt(data)

        return {
            "mode": "CTR",
            "iv": None,
            "nonce":
                base64.b64encode(nonce).decode(),
            "tag": None,
            "ciphertext":
                base64.b64encode(ciphertext).decode()
        }

    # ==================================================
    # EAX
    # ==================================================
    elif mode_choice == "6":

        nonce = get_random_bytes(16)

        cipher = AES.new(
            key,
            AES.MODE_EAX,
            nonce=nonce
        )

        ciphertext, tag = cipher.encrypt_and_digest(data)

        return {
            "mode": "EAX",
            "iv": None,
            "nonce":
                base64.b64encode(nonce).decode(),
            "tag":
                base64.b64encode(tag).decode(),
            "ciphertext":
                base64.b64encode(ciphertext).decode()
        }

    # ==================================================
    # GCM
    # ==================================================
    elif mode_choice == "7":

        nonce = get_random_bytes(12)

        cipher = AES.new(
            key,
            AES.MODE_GCM,
            nonce=nonce
        )

        ciphertext, tag = cipher.encrypt_and_digest(data)

        return {
            "mode": "GCM",
            "iv": None,
            "nonce":
                base64.b64encode(nonce).decode(),
            "tag":
                base64.b64encode(tag).decode(),
            "ciphertext":
                base64.b64encode(ciphertext).decode()
        }

    # ==================================================
    # CCM
    # ==================================================
    elif mode_choice == "8":

        nonce = get_random_bytes(11)

        cipher = AES.new(
            key,
            AES.MODE_CCM,
            nonce=nonce
        )

        ciphertext, tag = cipher.encrypt_and_digest(data)

        return {
            "mode": "CCM",
            "iv": None,
            "nonce":
                base64.b64encode(nonce).decode(),
            "tag":
                base64.b64encode(tag).decode(),
            "ciphertext":
                base64.b64encode(ciphertext).decode()
        }

    # ==================================================
    # SIV
    # ==================================================
    elif mode_choice == "9":

        # SIV requires double-length key:
        # 32 bytes -> AES-SIV-128
        # 48 bytes -> AES-SIV-192
        # 64 bytes -> AES-SIV-256

        if len(key) == 16:
            key = key + key

        elif len(key) == 24:
            key = key + key

        elif len(key) == 32:
            key = key + key

        cipher = AES.new(
            key,
            AES.MODE_SIV
        )

        ciphertext, tag = cipher.encrypt_and_digest(data)

        return {
            "mode": "SIV",
            "iv": None,
            "nonce": None,
            "tag":
                base64.b64encode(tag).decode(),
            "ciphertext":
                base64.b64encode(ciphertext).decode()
        }


def decrypt_aes(
    ciphertext_b64,
    key,
    mode,
    iv_b64=None,
    nonce_b64=None,
    tag_b64=None
):

    ciphertext = base64.b64decode(ciphertext_b64)

    # ==================================================
    # ECB
    # ==================================================
    if mode == "ECB":

        cipher = AES.new(
            key,
            AES.MODE_ECB
        )

        plaintext = cipher.decrypt(ciphertext)

        return unpad(
            plaintext,
            BLOCK_SIZE
        ).decode()

    # ==================================================
    # CBC
    # ==================================================
    elif mode == "CBC":

        iv = base64.b64decode(iv_b64)

        cipher = AES.new(
            key,
            AES.MODE_CBC,
            iv=iv
        )

        plaintext = cipher.decrypt(ciphertext)

        return unpad(
            plaintext,
            BLOCK_SIZE
        ).decode()

    # ==================================================
    # CFB
    # ==================================================
    elif mode == "CFB":

        iv = base64.b64decode(iv_b64)

        cipher = AES.new(
            key,
            AES.MODE_CFB,
            iv=iv
        )

        plaintext = cipher.decrypt(ciphertext)

        return plaintext.decode()

    # ==================================================
    # OFB
    # ==================================================
    elif mode == "OFB":

        iv = base64.b64decode(iv_b64)

        cipher = AES.new(
            key,
            AES.MODE_OFB,
            iv=iv
        )

        plaintext = cipher.decrypt(ciphertext)

        return plaintext.decode()

    # ==================================================
    # CTR
    # ==================================================
    elif mode == "CTR":

        nonce = base64.b64decode(nonce_b64)

        cipher = AES.new(
            key,
            AES.MODE_CTR,
            nonce=nonce
        )

        plaintext = cipher.decrypt(ciphertext)

        return plaintext.decode()

    # ==================================================
    # EAX
    # ==================================================
    elif mode == "EAX":

        nonce = base64.b64decode(nonce_b64)
        tag = base64.b64decode(tag_b64)

        cipher = AES.new(
            key,
            AES.MODE_EAX,
            nonce=nonce
        )

        plaintext = cipher.decrypt_and_verify(
            ciphertext,
            tag
        )

        return plaintext.decode()

    # ==================================================
    # GCM
    # ==================================================
    elif mode == "GCM":

        nonce = base64.b64decode(nonce_b64)
        tag = base64.b64decode(tag_b64)

        cipher = AES.new(
            key,
            AES.MODE_GCM,
            nonce=nonce
        )

        plaintext = cipher.decrypt_and_verify(
            ciphertext,
            tag
        )

        return plaintext.decode()

    # ==================================================
    # CCM
    # ==================================================
    elif mode == "CCM":

        nonce = base64.b64decode(nonce_b64)
        tag = base64.b64decode(tag_b64)

        cipher = AES.new(
            key,
            AES.MODE_CCM,
            nonce=nonce
        )

        plaintext = cipher.decrypt_and_verify(
            ciphertext,
            tag
        )

        return plaintext.decode()

    # ==================================================
    # SIV
    # ==================================================
    elif mode == "SIV":

        if len(key) == 16:
            key = key + key

        elif len(key) == 24:
            key = key + key

        elif len(key) == 32:
            key = key + key

        tag = base64.b64decode(tag_b64)

        cipher = AES.new(
            key,
            AES.MODE_SIV
        )

        plaintext = cipher.decrypt_and_verify(
            ciphertext,
            tag
        )

        return plaintext.decode()


def main():

    print("=" * 60)
    print("                 AES ENCRYPTION")
    print("=" * 60)

    key = get_key()

    mode_choice = choose_mode()

    plaintext = input("\nEnter plaintext: ")

    try:

        result = encrypt_aes(
            plaintext,
            key,
            mode_choice
        )

        print("\n" + "=" * 60)
        print("                    ENCRYPTION")
        print("=" * 60)

        print("Mode       :", result["mode"])
        print("IV         :", result["iv"])
        print("Nonce      :", result["nonce"])
        print("Tag        :", result["tag"])
        print("Ciphertext :", result["ciphertext"])

        print("\n" + "=" * 60)
        print("                    DECRYPTION")
        print("=" * 60)

        decrypted = decrypt_aes(
            result["ciphertext"],
            key,
            result["mode"],
            result["iv"],
            result["nonce"],
            result["tag"]
        )

        print("Plaintext  :", decrypted)

    except Exception as e:

        print("ERROR:", e)


if __name__ == "__main__":
    main()
