# Create a function to check if a number is a Prime number
def is_prime(num):
    
    # Prime numbers are numbers that can only be cleanly divided by themselves and 1.
    
    if num <= 1:
        return False  # 0 and 1 are not prime numbers
    
    for i in range(2, int(num ** 0.5) + 1):
        
        if num % i == 0:
            return False
        
    return True
        
        
# Check the function
is_prime(7)