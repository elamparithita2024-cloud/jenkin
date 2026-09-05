import sys

def main():
    print("--- Basic Python Application ---")
    
    # Check for command line arguments, otherwise use default numbers for CI automation
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
        except ValueError:
            print("Error: Please provide valid numbers.")
            sys.exit(1)
    else:
        print("No arguments provided. Using default values for automation.")
        num1 = 5
        num2 = 10

    # Calculate and display the sum
    total_sum = num1 + num2
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"The sum is: {total_sum}")
    print("Application executed successfully!")

if __name__ == "__main__":
    main()
