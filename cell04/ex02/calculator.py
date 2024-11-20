#!/usr/bin/env python
def calculator():
  num1 = float(input("Give me the first number: "))
  num2 = float(input("Give me the second number: "))

  print(f"Thank you!")
  print(f"{num1} + {num2} = {num1 + num2}")
  print(f"{num1} - {num2} = {num1 - num2}")
  print(f"{num1} / {num2} = {num1 / num2}")
  print(f"{num1} * {num2} = {num1 * num2}")

if __name__ == "__main__":
  calculator()