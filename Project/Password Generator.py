import pandas as pd
import random
import string
import sys
import os


# A function to shuffle all the characters of a string
def shuffle(s):
    temp_list = list(s)
    random.shuffle(temp_list)
    return "".join(temp_list)


# Function for generating passwords
def pass_generator():
    upper_letter1 = random.choice(
        string.ascii_uppercase
    )  # Generate a random Uppercase letter
    upper_letter2 = random.choice(
        string.ascii_uppercase
    )  # Generate a random Uppercase letter

    lower_letter1 = chr(
        random.randint(97, 122)
    )  # Generate a random Lowercase letter with ASCII code
    lower_letter2 = chr(
        random.randint(97, 122)
    )  # Generate a random Lowercase letter with ASCII code

    digit1 = chr(random.randint(48, 57))  # Generate a random number with ASCII code
    digit2 = chr(random.randint(48, 57))  # Generate a random number with ASCII code

    punctuation1 = random.choice(string.punctuation)  # Generate a random punctuation
    punctuation2 = random.choice(string.punctuation)  # Generate a random punctuation

    filler1 = random.choice(string.digits)  # Generate a random digit for filler
    filler2 = random.choice(
        string.ascii_letters
    )  # Generate a random uppercase or lowercase letter for filler

    # Generate password using all the characters, in random order
    return (
        upper_letter1
        + upper_letter2
        + lower_letter1
        + lower_letter2
        + digit1
        + digit2
        + punctuation1
        + punctuation2
        + filler1
        + filler2
    )


while True:
    try:
        n = input("\nHow many passwords do you want: ")

        try:
            number = int(n)  # Attempt to convert input to an integer
            if number <= 0:
                print("Error: Please enter a positive integer.")
                continue
        except ValueError:
            print(f"Error: '{n}' is not a valid number. Please enter a valid integer.")
            continue  # Ask for input again if it's not valid

        pass_list = []  # Reset the password list for each new input

        # Calling the defined functions to generate and shuffle passwords
        for i in range(number):
            password = shuffle(pass_generator())
            pass_list.append(password)

        # Create DataFrame
        df = pd.DataFrame(pass_list, columns=["Passwords"])
        df.index += 1  # To start the index at 1

        # Define the file name
        base_name = "generated_passwords"
        num = 1

        # Create a unique filename
        while True:
            name = f"{base_name}_{num}.xlsx"
            if not os.path.exists(name):  # Check if the file already exists
                break
            num += 1

        # Write the DataFrame to Excel
        df.to_excel(name)

        # Re-open the file with xlsxwriter engine to adjust column width
        with pd.ExcelWriter(name, engine="xlsxwriter") as writer:
            df.to_excel(writer)

            # Access the workbook and worksheet objects
            workbook = writer.book
            worksheet = writer.sheets["Sheet1"]

            # Set the width of a specific column
            worksheet.set_column("A:A", 5)  # Adjust the width of the 'Passwords' column
            worksheet.set_column("B:B", 15)
        print(f"Your passwords are saved to: {name}")

    except EOFError:
        sys.exit("\nInvalid input. Use integers.")

    except KeyboardInterrupt:
        sys.exit("\n\nProgram closed by user.")
