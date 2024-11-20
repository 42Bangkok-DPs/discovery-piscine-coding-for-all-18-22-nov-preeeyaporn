#!/usr/bin/env python
def print_multiplication_table(number):
  """พิมพ์ตารางสูตรคูณของจำนวนที่กำหนด

  Args:
    number: จำนวนที่ต้องการสร้างตารางสูตรคูณ
  """

  print(f"Table de {number}: ", end="")
  for i in range(11):
    print(f"{number*i:3}", end="")
  print()

if __name__ == "__main__":
  for i in range(1, 11):
    print_multiplication_table(i)