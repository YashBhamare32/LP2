import math

message = int(input("Enter the message to be encrypted: "))

p = 53
q = 59
n = p * q
phi = (p - 1) * (q - 1)

# Find e
for e in range(2, phi):
    if math.gcd(e, phi) == 1:
        break

# Find d
for i in range(phi):
    if (e * i) % phi == 1:
        d = i
        break

def encrypt(me):
    c = pow(me, e, n)
    return c

def decrypt(ct):
    p = pow(ct, d, n)
    return p

print("Original Message is: ", message)
CT = encrypt(message)
print("Encrypted Message is: ", CT)
PT = decrypt(CT)
print("Decrypted Message is:", PT)
