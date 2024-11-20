def multiply_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = num1 * num2

    if result > 0:
        print(f"{num1} x {num2} = {result}")
        print("The result is positive.")
    elif result < 0:
        print(f"{num1} x {num2} = {result}")
        print("The result is negative.")
    else:
        print(f"{num1} x {num2} = {result}")
        print("The result is zero.")

if __name__ == "__main__":
    multiply_numbers()