#!/usr/bin/env python
def count_to_25():
  while True:
    try:
      num = int(input("Enter a number less than 25: "))
      if num > 25:
        print("Error")
      else:
        for i in range(num, 26):
          print(f"Inside the loop, my variable is {i}")
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  count_to_25()