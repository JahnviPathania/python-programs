 #exception handling is a process of responding to unwannted or unexpected events when a computer program runs
#python has built in exception functiosn that are raised when your program encounters an error
#the built in function is try except block
 #example for try except

    # Taking input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    
    result = num1 / num2
    print("Result:", result)

# Handling division by zero
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Handling invalid number input
except ValueError:
    print("Error: Please enter valid numbers only.")

# Handling any other error
except Exception as e:
    print("Unexpected Error:", e)

# Code after try-except will still run
print("Program completed")
