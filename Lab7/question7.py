def make_withdraw(balance, password):
    """Return a password-protected withdraw function.
    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    lst = []
    attempts = 0
    def withdraw(amount, passcode):
        nonlocal balance, lst, attempts
        if attempts >= 3:
           return f"Your account is locked. Attempts: {lst}"
        if passcode != password:
            lst.append(passcode)
            attempts += 1
            return 'Incorrect password'
        if amount > balance:
            return 'Insufficient funds'
        balance -= amount
        return balance
    return withdraw
    