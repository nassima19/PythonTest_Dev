"""Module providingFunction printing python version."""

def add(x_values,y_values):
    """A dummy docstring.""" 
    z_values=x_values + y_values
    return z_values


def sus(x_values,y_values):
    """A dummy docstring."""
    z_values=x_values - y_values
    return z_values

def multiplication(x_values,y_values):
    """A dummy docstring."""
    z_values=x_values*y_values
    return z_values


def fact(num):
    """A dummy docstring."""
    factorial = 1
    # check if the number is negative, positive or zero


    if num < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
        return factorial
    return None
