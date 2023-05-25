def is_prime(n): 
    """
    >>> is_prime(7) 
    True
    >>> is_prime(10) 
    False
    >>> is_prime(1) 
    False
    >>> is_prime(2)
    """
    def prime_helper(n, i):
        if n == i: 
            return True
        elif n <= 1 or n % i == 0: 
            return False
        else:
            return prime_helper(n, i+1)        
    return prime_helper(n, 2)

# prime: >1, only divisible by itself and 1. (e.g. 2,3,5,7,11)
# check if number is equal to i (initially 2)
# else if <=1 (negative/0) or divisible by i
# else recurisve call function with i++.
# continues until the number n==i and means # is divisible
# by only itself.
# or goes to elif and number is divisible by some factor
