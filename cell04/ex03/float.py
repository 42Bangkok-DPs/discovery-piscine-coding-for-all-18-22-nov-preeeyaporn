#!/usr/bin/env python
def check_number_type():
  number = float(input("Give me a number: "))
  if number.is_integer():
    print("This number is an integer.")
  else:
    print("This number is a decimal.")

if __name__ == "__main__":
  check_number_type()