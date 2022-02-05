import secrets
import string

# This program generate a secure and random password
SEPARATOR = (
        "####################################################################"
    )


def menu():
    global SEPARATOR
    # Define the menu
    print(SEPARATOR)
    print("This program generate a secure and random password.")
    print("(Dont use whitespaces)")

    print(SEPARATOR)

    # Ask for a character limit
    while True:
        char_limit_ask = input(
            "Do you want to choose the character limit? (y/n): "
        )

        if char_limit_ask in ["y", "Y", "n", "N"]:
            break
        else:
            print("Please, enter a valid input.")

    # Define the character limit
    if char_limit_ask in ["Y", "y"]:
        while True:
            character_limit = input("How many characters do you want?: ")
            if character_limit.isnumeric():
                if int(character_limit) < 4:
                    print(
                        "Not enough characters for a password," +
                        "please enter a number greater than 4"
                    )
                else:
                    print(
                        "Your password will be",
                        int(character_limit),
                        "characters long"
                    )
                    limit = int(character_limit)
                    break
            else:
                print("Please, enter a valid number.")
    else:
        print("Your password will be 12 characters long.")
        print(SEPARATOR)
        limit = 12

    # Ask for special characters
    while True:
        spec_char_ask = input(
            "Do you want special characters? (Highly recommended) (y/n): "
        )
        if spec_char_ask in ["y", "Y", "n", "N"]:
            if spec_char_ask in ["y", "Y"]:
                spec_char = True
                print(SEPARATOR)
                break
            elif spec_char_ask in ["n", "N"]:
                spec_char = False
                print(SEPARATOR)
                break
        else:
            print("Please, enter a valid input.")

    # Ask for exclude characters
    while True:
        excl_char_ask = input("Do you want exclude some character? (y/n): ")
        if excl_char_ask in ["y", "Y", "n", "N"]:
            break
        else:
            print("Please, enter a valid input.")

    # Exclude characters
    if excl_char_ask in ["y", "Y"]:
        while True:
            list_excl_char = []
            whitespaces = 0
            excl_char = input(
                "Which characters do you want to exclude?(Example: &%/$#): "
            )
            # Separate the string in characters
            for i in range(len(excl_char)):
                list_excl_char.append(excl_char[i])

            for i in list_excl_char:
                if i in string.whitespace:
                    whitespaces += 1

            if whitespaces == 0:
                break
            else:
                excl_char
                print("Please, enter a valid input.")
        print(SEPARATOR)
    else:
        print(SEPARATOR)
        list_excl_char = []
    print("Loading...")
    if limit > 10000:
        print("The input number is very long, it could take a long time.")
    elections = {
        "char_limit": limit,
        "spec_char": spec_char,
        "excluded_chars": list_excl_char
    }
    return elections


def pass_generator(elections):
    # Generate the password
    # Dictionarie elements char_limit, spec_char, excluded_chars

    # Configuration of the number of characters per type
    # Determinate the alpha and numeric number of characters
    alpha_chars = []
    for i in range(2, elections["char_limit"]-1):
        alpha_chars.append(i)
    alpha_section = secrets.choice(alpha_chars)

    low_chars = []
    for i in range(1, alpha_section):
        low_chars.append(i)
    low_section = alpha_section - secrets.choice(low_chars)
    upp_section = alpha_section - low_section

    special_section = (elections["char_limit"]-alpha_section)

    if elections["spec_char"] is True:
        symbol_chars = []
        for i in range(1, special_section):
            symbol_chars.append(i)
        symbols_section = special_section - secrets.choice(symbol_chars)

    elif elections["spec_char"] is False:
        symbols_section = 0

    numeric_section = special_section - symbols_section

    # Determinate the password_characters

    # Lower alphabet characters setup
    low_alphabet = string.ascii_lowercase
    low_alphabet_list = []
    for i in range(len(low_alphabet)):
        if low_alphabet[i] not in elections["excluded_chars"]:
            low_alphabet_list.append(low_alphabet[i])

    # Upper alphabet characters setup
    upp_alphabet = string.ascii_uppercase
    upp_alphabet_list = []
    for i in range(len(upp_alphabet)):
        if upp_alphabet[i] not in elections["excluded_chars"]:
            upp_alphabet_list.append(upp_alphabet[i])

    # Number characters setup
    numbers = string.digits
    numbers_list = []
    for i in range(len(numbers)):
        if numbers[i] not in elections["excluded_chars"]:
            numbers_list.append(numbers[i])

    # Symbol characters setup
    symbols = string.punctuation
    symbols_list = []
    for i in range(len(symbols)):
        if symbols[i] not in elections["excluded_chars"]:
            symbols_list.append(symbols[i])

    password_chars = []
    for i in range(low_section):
        password_chars.append(str(secrets.choice(low_alphabet_list)))

    for i in range(upp_section):
        password_chars.append(secrets.choice(upp_alphabet_list))

    for i in range(numeric_section):
        password_chars.append(secrets.choice(numbers_list))

    for i in range(symbols_section):
        password_chars.append(secrets.choice(symbols_list))

    # Finally generate the password
    password = ""
    for i in range(elections["char_limit"]):
        actual_char = secrets.choice(password_chars)
        password += actual_char
        password_chars.remove(actual_char)
    return password


def pass_comprobation(password):
    # Check if the generated password is one of the most used worldwide
    passwords_list = open("insecure_passwords.txt", "r")

    if password in passwords_list.read():
        return True
    else:
        return False


def main():
    elections = menu()
    insecure_password = True
    while insecure_password is True:
        password = pass_generator(elections)
        insecure_password = pass_comprobation(password)

    global SEPARATOR
    print(SEPARATOR)
    print("Your unique generated password is:\n", password)
    print(SEPARATOR)

if __name__ == "__main__":
    main()
