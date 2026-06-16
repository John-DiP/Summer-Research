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

print(d)

message = input("Enter a message: ")

# Convert to character array
list = list(message)


print(list)

