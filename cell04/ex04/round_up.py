#!/usr/bin/env python
import math

def round_up_number():
  """ฟังก์ชันปัดเศษขึ้น"""
  number = float(input("Give me a number: "))
  rounded_up = math.ceil(number)
  print(f"{rounded_up}")

if __name__ == "__main__":
  round_up_number()