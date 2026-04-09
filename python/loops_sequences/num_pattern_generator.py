def number_pattern(n):
    """
    This function takes an integer n as input and returns
    a string containing the numbers from 1 to n, separated by spaces.
    """

    # Validate the input
    if not (isinstance(n,int)):
        return 'Argument must be an integer value.'
    if n < 1:
        return 'Argument must be an integer greater than 0.'

    # Return the numbers from 1 to n as a space-separated string
    return " ".join([str(i) for i in range(1, n + 1)])

print(number_pattern(4))