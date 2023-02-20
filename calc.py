# Simple calculator program in Python

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# Main function to get user input and perform calculations
def main():
    print("Welcome to the calculator program!")
    print("Please choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    # Get user input for operation
    choice = int(input("Enter your choice (1-4): "))
    
    # Get user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Perform calculations based on user choice
    if choice == 1:
        result = add(num1, num2)
        print("The result is:", result)
    elif choice == 2:
        result = subtract(num1, num2)
        print("The result is:", result)
    elif choice == 3:
        result = multiply(num1, num2)
        print("The result is:", result)
    elif choice == 4:
        result = divide(num1, num2)
        print("The result is:", result)
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        
# Call the main function
main()
