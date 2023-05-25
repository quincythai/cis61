def count_digit(n, digit):
    """Return the number of times digit appears in n."""
    if n == 0:  # base case: no more digits to compare
        return 0
    last_digit = n % 10  # get the last digit of n
    if last_digit + digit == 10:  # if the last digit matches the desired digit
        return 1 + count_digit(n // 10, digit)  # count it and move on to the next digit
    else:
        return count_digit(n // 10, digit)  # move on to the next digit without counting

def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    """

    if n < 10:  # base case: single digit left, no possible pairs
        return 0
    last_digit = n % 10  # get the last digit of n
    remaining_digits = n // 10  # get the remaining digits of n
    count = count_digit(remaining_digits, last_digit)  # count the number of times the complement appears in the remaining digits
    return count + ten_pairs(remaining_digits)  # count the number of pairs in the remaining digits and add it to the current count
