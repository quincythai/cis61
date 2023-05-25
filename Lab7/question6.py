def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called. 0, 1, 1, 2, 3, 5, 8, 13,
    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    >>> fib2 = make_fib()
    >>> fib() + sum([fib2() for _ in range(5)])
    12
    """
    a = 0
    b = 1

    def fib():
        nonlocal a, b
        result = a # store current Fib number
        a = b # update a to next Fib number
        b += result # update b to next one (sum of previous two)
        return result

    return fib