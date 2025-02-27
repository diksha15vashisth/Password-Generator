import random
import string


def generate_password(length, include_special_chars=True):
   
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

   
    all_characters = lowercase + uppercase + digits
    if include_special_chars:
        all_characters += special_chars

   
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password


def password_generator():
    print("Welcome to the Password Generator!")

    while True:
        
        while True:
            try:
                length = int(input("\nEnter the length of the password (minimum 8 characters): "))
                if length < 8:
                    print("For security, please choose a password length of at least 8 characters.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

       
        while True:
            complexity = input("Do you want to include special characters (y/n)? ").lower()
            if complexity in ['y', 'n']:
                include_special_chars = True if complexity == 'y' else False
                break
            else:
                print("Please enter 'y' for yes or 'n' for no.")

   
        password = generate_password(length, include_special_chars)


        print(f"\nYour generated password is: {password}")

       
        continue_choice = input("\nDo you want to generate another password? (y/n): ").lower()
        if continue_choice != 'y':
            print("Thank you for using the Password Generator!")
            break

# Run the password generator
if __name__ == "__main__":
    password_generator()
