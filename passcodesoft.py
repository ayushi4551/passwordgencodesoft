import random
import string


# Function to generate a random password
def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password


# Main function to drive the password generator
def main():
    # Prompt user for the desired length of the password
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    # Generate the password
    password = generate_password(length)

    # Display the password
    print(f"Generated password: {password}")


# Run the main function
if __name__ == "__main__":
    main()
