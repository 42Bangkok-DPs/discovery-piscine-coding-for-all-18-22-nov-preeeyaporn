#!/usr/bin/env python
def main():
  while True:
    user_input = input("What you gotta say? ")
    if user_input.lower() == "stop":
      break
    print("I got that! Anything else?")

if __name__ == "__main__":
  main()