from cryptography.hazmat.primitives.asymmetric import rsa


def generate_rsa_key():
    name = input("Enter system name: ")

    if name not in systems:
        print("System not registered")
        return

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    systems[name] = {
        "private": private_key,
        "public": public_key
    }

    print("RSA key pair generated for", name)
