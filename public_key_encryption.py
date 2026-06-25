# Code for public key encryption using RSA

import math
import time

def get_d(k):
    d = k - 1
    
    while d > 1:
        if math.gcd(d, k) == 1:
            return d
        else:
            d -= 1


def main():
    p = int(input("Enter the first prime number: "))
    q = int(input("Enter the second prime number: "))

    n = p * q
    k = (p - 1) * (q - 1)

    d = get_d(k)

    #   Find x, again with d you can run through all i from 2 to k-1 d*x=1 mod k. 

    #	Once you found x you can decrypt the message.  

    #   Equation: dx ≡ 1 mod p

    for x in range(2, k - 1):
        if ((d * x) % k == 1):
            break

    # encrypt
    encrypt = (19 ** d) % n  

    start_time = time.perf_counter()

    # decrypt
    decrypt = (encrypt ** x) % n

    end_time = time.perf_counter()

    time_in_seconds = end_time - start_time

    print("First prime:" + str(p))
    print("second prime:" + str(q))
    print("d: " + str(d))
    print("x: " + str(x))
    print("Encrypted: " + str(encrypt))
    print("Decrypted: " + str(decrypt))
    print("Seconds: " +str(time_in_seconds))

main()