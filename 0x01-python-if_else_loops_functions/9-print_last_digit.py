#!/usr/bin/python3
def print_last_digit(number):
  last_digit = abs(number) % 10
  if last_digit == 0:
    return(0)
    print("0")
  else:
    return(last_digit)
    print(last_digit)
