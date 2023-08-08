#!/usr/bin/python3
def print_last_digit(number):
    last_digit_of_num = abs(number) % 10
    print(f"{last_digit_of_num}", end='')
    return last_digit_of_num
