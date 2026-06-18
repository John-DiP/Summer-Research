# Code for public key encryption using RSA

import math

p = int(input("Enter the first prime number: "))
q = int(input("Enter the second prime number: "))

d = 2

n = p * q
k = (p - 1) * (q - 1)


while (d < k):
    if (math.gcd(d, k) == 1):
        break
    else:
        d +=1


#   Step 1: it needs to calculate k=(p-1)*(q-1) – so it will have to factor p*q as p and q the two primes that make it up. 
#   A stupid way to do this is to do a while loop i from 2 to n-1 and take n mod i 
#   if that = 0 then i divides n and you have found a prime p after you find one you can just divide to get the other prime q. 


#i = 2

# still need to work on this
#while (i < (n-1)):
    #if (n % i) == 0:
        #p = i
        #q = n / p
        #break
    #i += 1


#   Find x, again with d you can run through all i from 2 to k-1 d*x=1 mod k. 

#	Once you found x you can decrypt the message.  

# Equation: dx ≡ 1 mod p

for x in range(2, k - 1):
    if ((d * x) % k == 1):
        break
    

#print("i: " + str(i))
print("First prime:" + str(p))
print("second prime:" + str(q))
print("d: " + str(d))
print("x: " + str(x))