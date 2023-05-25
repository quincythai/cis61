def is_prime(n): 
    """
    >>> is_prime(7) 
    True
    >>> is_prime(10) 
    False
    >>> is_prime(1) 
    False
    >>> is_prime(2)
    True
    """
    def prime_helper(k):
        if n == k:
            return True
        elif n % k == 0 or n == 1:
            return False
        else:
            return prime_helper(k + 1)
    return prime_helper(2)