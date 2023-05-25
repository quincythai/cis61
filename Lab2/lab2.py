def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    divisor = n - 1
    while (n % divisor != 0):
        divisor -= 1
    return divisor == 1

    #method: see if there is a factor that divides evenly into n.
    # if loop ends and divisor is 1, then prime #