
import secrets


def get_password_length():
    while True:
        try:
            length = int(input("How many characters do you want? "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if length <= 0:
            print("Number must be greater than zero!")
            continue

        return length


def get_yes_no(question):
    while True:
        answer = input(question).lower()

        if answer in ("y", "n"):
            return answer

        print("Please enter y or n!")


def generate_password(length, characters):
    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password


def main():
    print("Welcome to Password Generator!")

    password_length = get_password_length()

    characters = {
        "lowercase": "abcdefghijklmnopqrstuvwxyz",
        "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "numbers": "0123456789",
        "symbols": "!@#$%^&*()"
    }

    all_characters = ""

    if get_yes_no("Include lowercase letters? (y/n): ") == "y":
        all_characters += characters["lowercase"]

    if get_yes_no("Include uppercase letters? (y/n): ") == "y":
        all_characters += characters["uppercase"]

    if get_yes_no("Include numbers? (y/n): ") == "y":
        all_characters += characters["numbers"]

    if get_yes_no("Include symbols? (y/n): ") == "y":
        all_characters += characters["symbols"]

    if not all_characters:
        print("Error: You must select at least one character type!")
        return

    password = generate_password(password_length, all_characters)

    print(f"Your generated password is: {password}")


if __name__ == "__main__":
    main()
