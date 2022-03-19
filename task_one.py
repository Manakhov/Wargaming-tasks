def isEven(value):
    return value % 2 == 0


def is_even(value):
    if value & 1:
        return False
    else:
        return True
