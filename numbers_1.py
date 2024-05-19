import math

# Function to check if a number is even
def even(num):
    return num % 2 == 0

# Function to check if a number has a perfect square root
def perfect_square_root(num):
    sqrt = math.sqrt(num)
    return int(sqrt) == sqrt

# Function to find all factors of a number
def factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

# Main function to interact with the user
def main():
    play = True
    while play:
        # Prompt the user to enter a whole number
        num_input = input("Please enter a whole number (i.e. an integer): ")
        if num_input.isdigit():
            num = int(num_input)
            print(f"The number you entered is {num}.")
        else:
            print("That's not a valid integer. Please try again.")
            continue

        # Check if the number is even or odd
        if even(num):
            print(f"{num} is an even number.")
        else:
            print(f"{num} is an odd number.")

        # Check if the number has a perfect square root
        if perfect_square_root(num):
            print(f"{num} has a perfect square root.")
        else:
            print(f"{num} does not have a perfect square root.")

        # Find and print all factors of the number
        factors_list = factors(num)
        factors_str = ', '.join(map(str, factors_list))
        print(f"The factors of {num} are {factors_str}.")

        # Ask the user if they want to enter another number
        another = input("Would you like to enter another number? (y/n): ").strip().lower()
        if another == 'n':
            print("Thank you for playing!")
            break

# Run the main function if the script is executed
if __name__ == "__main__":
    main()
