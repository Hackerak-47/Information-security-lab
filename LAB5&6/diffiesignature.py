import secrets


# Public parameters
p = 23
g = 5


# Alice generates private and public keys
def alice_keys():
    private_key = secrets.randbelow(p - 2) + 1
    public_key = pow(g, private_key, p)

    return private_key, public_key


# Bob generates private and public keys
def bob_keys():
    private_key = secrets.randbelow(p - 2) + 1
    public_key = pow(g, private_key, p)

    return private_key, public_key


# Generate shared secret
def generate_shared_secret(private_key, other_public_key):
    return pow(other_public_key, private_key, p)


# Main
alice_private, alice_public = alice_keys()
bob_private, bob_public = bob_keys()

print("Alice private key:", alice_private)
print("Alice public key:", alice_public)

print("Bob private key:", bob_private)
print("Bob public key:", bob_public)


# Exchange public keys
alice_shared = generate_shared_secret(
    alice_private,
    bob_public
)

bob_shared = generate_shared_secret(
    bob_private,
    alice_public
)

print("Alice shared secret:", alice_shared)
print("Bob shared secret:", bob_shared)


# Verify
if alice_shared == bob_shared:
    print("Shared secret is same")
else:
    print("Shared secret is different")
