#!/usr/bin/env python
def convert_to_uppercase():
  """แปลงข้อความให้เป็นตัวพิมพ์ใหญ่"""
  word = input("Give me a word: ")
  uppercase_word = word.upper()
  print(uppercase_word)

if __name__ == "__main__":
  convert_to_uppercase()