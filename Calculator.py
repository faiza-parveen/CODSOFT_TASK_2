#!/usr/bin/env python
# coding: utf-8

# In[1]:


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculator():
    print("Simple Calculator")

    # Input two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Input the operation choice
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    try:
        choice = int(input("Enter choice (1-4): "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Perform the calculation based on the user's choice
    if choice == 1:
        result = add(num1, num2)
        operator = "+"
    elif choice == 2:
        result = subtract(num1, num2)
        operator = "-"
    elif choice == 3:
        result = multiply(num1, num2)
        operator = "*"
    elif choice == 4:
        result = divide(num1, num2)
        operator = "/"
    else:
        print("Invalid choice. Please select a valid operation.")
        return

    # Display the result
    print(f"\nResult: {num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()


# In[ ]:




