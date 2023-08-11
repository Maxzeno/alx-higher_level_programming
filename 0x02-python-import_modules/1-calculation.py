#!/usr/bin/python3

if __name__ == "__main__":
    """Print the add, sub, mul and div of two numbers."""
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    print("{a} + {b} = {sum}".format(a=a, b=b, sum=add(a, b)))
    print("{a} - {b} = {sum}".format(a=a, b=b, sum=sub(a, b)))
    print("{a} * {b} = {sum}".format(a=a, b=b, sum=mul(a, b)))
    print("{a} / {b} = {sum}".format(a=a, b=b, sum=div(a, b)))
