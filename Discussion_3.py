import math

p = 5
q = 11

d = 3

n = p * q
k = (p - 1) * (q - 1)

for x in range(2, k-1):
    if ((d * x) % k == 1):
        break

# encrypt
encrypt = (19 ** d) % n

# decrypt
decrypt = (encrypt ** x) % n

print ("Decrypted: " + str(decrypt))

# to answer the question, in order to decrypt this, we would take the encrypted value 
# use x as a exponent, and then use modulus on the value with n
