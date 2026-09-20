p = 23
g = 5

a = 6
A = pow(g, a, p)

b = 15
B = pow(g, b, p)

alice_shared = pow(B, a, p)
bob_shared = pow(A, b, p)
