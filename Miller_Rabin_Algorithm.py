# implementation using Miller-Rabin

# https://github.com/John-DiP/Summer-Research Github repository for summer research code
import time
import math
import random

def miller_rabin(n, k=10):
    if n == 2 or n == 3:
        return True
 
    if n <= 1 or n % 2 == 0:
        return False
 
    d = n - 1
    r = 0
 
    while d % 2 == 0:
        d //= 2
        r += 1
 
    for _ in range(k):
 
        a = random.randrange(2, n - 2)
        x = pow(a, d, n)
 
        if x == 1 or x == n - 1:
            continue
 
        for _ in range(r - 1):
            x = pow(x, 2, n)
 
            if x == n - 1:
                break
 
        else:
            return False
 
    return True

def generate_prime(lower, upper):
    while True:
        candidate = random.randrange(lower, upper)

        if candidate %  2 == 0:
            candidate += 1

        if candidate > upper or candidate < lower:
            continue

        if miller_rabin(candidate):
            return candidate

def get_e(phi):
    e = 65537

    if math.gcd(e, phi) == 1:
        return e
    e = 3
    
    while math.gcd(e, phi) != 1:
        e += 2
    return e

def get_d(e, phi):
    return pow(e, -1, phi)

def brute_force_factor(n):
    
    if n % 2 == 0:
        return 2
    f = 3
    limit = math.isqrt(n) + 1
    while f <= limit:
        if n % f == 0:
            return f
        f += 2
    return None
 
 
def decrypt(ciphertext, n, e):
    start = time.perf_counter()
 
    # Brute force the private key by factoring n, then decrypt.
    p = brute_force_factor(n)
    q = n // p
    phi = (p - 1) * (q - 1)
    d = get_d(e, phi)
    plaintext = pow(ciphertext, d, n)
 
    end = time.perf_counter()
    return plaintext, end - start
 
 
def run_trials(lower, upper, trials=10, message=42):
    p = generate_prime(lower, upper)
    q = generate_prime(lower, upper)
    while q == p:
        q = generate_prime(lower, upper)
 
    n = p * q
    phi = (p - 1) * (q - 1)
    e = get_e(phi)
    ciphertext = pow(message, e, n)
 
    times = []
    for _ in range(trials):
        recovered, elapsed = decrypt(ciphertext, n, e)
        assert recovered == message, "Decryption failed!"
        times.append(elapsed)
 
    avg_time = sum(times) / len(times)
    return p, q, n, avg_time
 
 
def main():
 
    ranges = [
        (1, 100),
        (100, 1000),
        (1000, 10000),
        (10000, 100000)
    ]
 
    print("Results: \n")
    print(f"{'A (low)':>10} | {'B (high)':>10} | {'Avg Decrypt Time (s)':>22}")
    print("-" * 50)
 
    for lower, upper in ranges:
        p, q, n, avg_time = run_trials(lower, upper)
        print(f"{lower:>10} | {upper:>10} | {avg_time:>22.8f}")
        
main()