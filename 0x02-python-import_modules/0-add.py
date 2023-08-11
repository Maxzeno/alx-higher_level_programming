#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of two numbers"""
    from add_0 import add

    a = 1
    b = 2
    print("{a} + {b} = {sum}".format(a=a, b=b, sum=add(a, b)))
