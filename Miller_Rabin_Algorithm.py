# implementation using Miller-Rabin

# https://github.com/John-DiP/Summer-Research Github repository for summer research code

def miller_rabin(n):

    if n == 2 or n == 3:
        return True
    
    if n < 2 or n % 2 == 0:
        return False
    
    d = n - 1
    s = 0

    

def main():
    while(True):
    
        n = int(input("Enter a number: "))
        
        miller_rabin(n)

main()