import secrets
import hashlib
from math import gcd


# ============================================================
# KEY MANAGEMENT SYSTEM
# ============================================================

class KeyManagementSystem:

    def __init__(self):
        self.systems = {}

    # Register a new subsystem
    def register_system(self, system_name):
        if system_name in self.systems:
            print("System already registered.")
            return

        # Generate RSA keys
        p = 61
        q = 53

        n = p * q
        phi = (p - 1) * (q - 1)

        e = 17
        d = pow(e, -1, phi)

        self.systems[system_name] = {
            "rsa_public": (n, e),
            "rsa_private": (n, d),
            "status": "ACTIVE"
        }

        print(system_name, "registered successfully.")

    # Get public key for distribution
    def get_public_key(self, system_name):
        if system_name not in self.systems:
            return None

        if self.systems[system_name]["status"] == "REVOKED":
            return None

        return self.systems[system_name]["rsa_public"]

    # Revoke a system's key
    def revoke_key(self, system_name):
        if system_name in self.systems:
            self.systems[system_name]["status"] = "REVOKED"
            print("Keys of", system_name, "have been revoked.")
        else:
            print("System not found.")

    # Display all systems
    def display_systems(self):
        print("\n===== REGISTERED SYSTEMS =====")

        for name, data in self.systems.items():
            print(
                name,
                "->",
                data["status"],
                "| Public Key:",
                data["rsa_public"]
            )


# ============================================================
# RSA ENCRYPTION
# ============================================================

def rsa_encrypt(message, public_key):

    n, e = public_key

    encrypted = []

    for ch in message:
        m = ord(ch)

        if m >= n:
            raise ValueError("Message character is too large for RSA key.")

        c = pow(m, e, n)

        encrypted.append(c)

    return encrypted


# ============================================================
# RSA DECRYPTION
# ============================================================

def rsa_decrypt(ciphertext, private_key):

    n, d = private_key

    message = ""

    for c in ciphertext:
        m = pow(c, d, n)

        message += chr(m)

    return message


# ============================================================
# DIFFIE-HELLMAN KEY EXCHANGE
# ============================================================

def diffie_hellman():

    # Public parameters
    p = 467
    g = 2

    print("\n===== DIFFIE-HELLMAN KEY EXCHANGE =====")

    # Private values
    a = secrets.randbelow(p - 2) + 1
    b = secrets.randbelow(p - 2) + 1

    # Public values
    A = pow(g, a, p)
    B = pow(g, b, p)

    # Shared secrets
    secret_A = pow(B, a, p)
    secret_B = pow(A, b, p)

    print("Alice public value :", A)
    print("Bob public value   :", B)

    print("Alice shared secret:", secret_A)
    print("Bob shared secret  :", secret_B)

    if secret_A == secret_B:
        print("Diffie-Hellman key exchange successful.")

    # Convert shared secret into a cryptographic key
    shared_key = hashlib.sha256(
        str(secret_A).encode()
    ).hexdigest()

    print("Derived shared key :", shared_key)

    return shared_key


# ============================================================
# MAIN PROGRAM
# ============================================================

kms = KeyManagementSystem()

while True:

    print("\n===================================")
    print("       SECURECORP SYSTEM")
    print("===================================")

    print("1. Register new subsystem")
    print("2. Display registered systems")
    print("3. Establish Diffie-Hellman connection")
    print("4. Send encrypted document")
    print("5. Revoke subsystem")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # --------------------------------------------------------
    # Register
    # --------------------------------------------------------

    if choice == "1":

        name = input("Enter subsystem name: ")

        kms.register_system(name)

    # --------------------------------------------------------
    # Display
    # --------------------------------------------------------

    elif choice == "2":

        kms.display_systems()

    # --------------------------------------------------------
    # Diffie-Hellman
    # --------------------------------------------------------

    elif choice == "3":

        system1 = input("Enter first system: ")
        system2 = input("Enter second system: ")

        if system1 not in kms.systems or system2 not in kms.systems:
            print("One or both systems are not registered.")

        elif (
            kms.systems[system1]["status"] == "REVOKED"
            or kms.systems[system2]["status"] == "REVOKED"
        ):
            print("Communication denied. One system is revoked.")

        else:
            print(
                "\nEstablishing secure connection between",
                system1,
                "and",
                system2
            )

            diffie_hellman()

    # --------------------------------------------------------
    # Encrypt and send document
    # --------------------------------------------------------

    elif choice == "4":

        sender = input("Enter sender system: ")
        receiver = input("Enter receiver system: ")

        if sender not in kms.systems:
            print("Sender not registered.")

        elif receiver not in kms.systems:
            print("Receiver not registered.")

        elif (
            kms.systems[sender]["status"] == "REVOKED"
            or kms.systems[receiver]["status"] == "REVOKED"
        ):
            print("Communication denied. Key has been revoked.")

        else:

            document = input("Enter document/message: ")

            public_key = kms.get_public_key(receiver)

            private_key = kms.systems[receiver]["rsa_private"]

            # RSA Encryption
            encrypted = rsa_encrypt(
                document,
                public_key
            )

            print("\nEncrypted document:")
            print(encrypted)

            # RSA Decryption
            decrypted = rsa_decrypt(
                encrypted,
                private_key
            )

            print("\nDecrypted document:")
            print(decrypted)

    # --------------------------------------------------------
    # Revoke
    # --------------------------------------------------------

    elif choice == "5":

        system = input("Enter system to revoke: ")

        kms.revoke_key(system)

    # --------------------------------------------------------
    # Exit
    # --------------------------------------------------------

    elif choice == "6":

        print("SecureCorp system terminated.")
        break

    else:

        print("Invalid choice.")
