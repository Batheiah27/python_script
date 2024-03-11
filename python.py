# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Main function
def main():
    print("Welcome to the Add Two Numbers Program!")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = add_numbers(num1, num2)
        print("The sum of", num1, "and", num2, "is:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

# Call the main function to run the program
if __name__ == "__main__":
    main()


