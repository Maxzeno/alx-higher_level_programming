#!/usr/bin/python3

if __name__ == '__main__':
    """Print the sum of nums pass as args."""
    import sys

    result = 0
    for i in sys.argv[1:]:
        result += int(i)
    print("{}".format(result))
