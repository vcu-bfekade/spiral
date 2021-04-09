def spiralize(number):
    return_value = 1
    n = (number - 1) / 2
    z = (3 + 2 * n * (8 * n * n + 15 * n + 13)) / 3
    return_value = z
    return return_value
