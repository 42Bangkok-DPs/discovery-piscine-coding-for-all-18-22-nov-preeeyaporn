#!/usr/bin/env python
def multiplication_table():
  """สร้างตารางสูตรคูณ"""
  number = int(input("Enter a number: "))

  for i in range(0, 10):
    print(f"{i} x {number} = {i * number}")

if __name__ == "__main__":
  multiplication_table()