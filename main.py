def divide_two_nums(num1: int, num2: int):
    """
    This function divides num1 into num2.
    :param num1:
    :param num2:
    :return: float
    """
    try:
        result = num1 / num2
    except ZeroDivisionError:
        return "You cannot divide by zero."
    else:
        return round(result, 2)
