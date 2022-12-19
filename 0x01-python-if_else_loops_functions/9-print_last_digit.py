#!/usr/bin/python3
def print_last_digit(number):
  last_digit = abs(number) % 10
<<<<<<< HEAD
  print(last_digit, end="")
  return (last_digit)
=======
  if last_digit == 0:
    return(0)
    print("0")
  else:
    return(last_digit)
    print(last_digit)
>>>>>>> 0ba116daa8a4e1ba3583cdb7175534c5866ab796
