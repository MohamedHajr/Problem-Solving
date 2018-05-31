def reverse(input=''):
    return input if len(input) == 0 else reverse(input[1:]) + input[0]
