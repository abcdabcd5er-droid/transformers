# Program: Add 20 Numbers and Display Details
# Author: Abhishek S Angadi
# Language: Python
# Description:
# This program accepts 20 numbers from the user, stores them in a list,
# calculates the total sum, average, highest, and lowest number.

def get_numbers(count):
    """Function to read 'count' numbers from the user"""
    numbers = []
    print(f"Enter {count} numbers:")
    for i in range(count):
        while True:
            try:
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    return numbers

def calculate_sum(numbers):
    """Function to calculate sum of a list of numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

def display_results(numbers, total):
    """Display detailed results"""
    print("\n===== RESULTS =====")
    print("Numbers entered:", numbers)
    print(f"Total Sum: {total}")
    print(f"Average: {total / len(numbers):.2f}")
    print(f"Maximum Number: {max(numbers)}")
    print(f"Minimum Number: {min(numbers)}")
    print("===================\n")

def main():
    print("=== Welcome to the 20 Number Adder Program ===\n")
    count = 20
    numbers = get_numbers(count)
    total = calculate_sum(numbers)
    display_results(numbers, total)

    # Optional feature: Ask if user wants to repeat
    while True:
        choice = input("Do you want to run again? (y/n): ").strip().lower()
        if choice == 'y':
            main()  # recursive restart
            break
        elif choice == 'n':
            print("\nThank you for using the program! Goodbye!")
            break
        else:
            print("Invalid choice! Please type 'y' or 'n'.")

# Entry point of the program
if __name__ == "__main__":
    main()
