import random
import pyperclip
import base64
from colorama import Fore, Back, Style


def add_password(identity, url, username, password):
    passinfo = "ID: " + identity + " Url: " + url + "  Username: " + username + "  Password: " + password + "\n"
    passinfo_bytes = base64.b64encode(passinfo.encode("utf-8"))
    enc_passinfo = str(passinfo_bytes, "utf-8")

    with open("passwords.txt", "a") as passfile:
        passfile.write(str(enc_passinfo))

    print(Fore.GREEN + '\nPassword Successfully Added!')
    print(Style.RESET_ALL)


def manage_passwords():
    quit = False
    option = ""
    while quit == False:
        print("\n1) View Passwords")
        print("2) Delete An Entry")
        print("3) Back To Main Menu")

        option = input("\nEnter an option: ")

        if option == "1":
            with open("passwords.txt", "r") as passfile:
                for line in passfile:
                    line = base64.b64decode(bytes(line, 'utf-8'))
                    line = str(line).strip("b'")
                    line = line[:-2]
                    print(Fore.GREEN + line)
                    print(Style.RESET_ALL)

        if option == "2":
            item_to_delete = int(input("\nEnter the line number for an entry: "))
            with open('passwords.txt', 'r') as passfile:
                lines = passfile.readlines()
                ptr = 1
                with open('passwords.txt', 'w') as passfile_w:
                    for line in lines:
                        if ptr != item_to_delete:
                            passfile_w.write(line)
                        ptr += 1

        if option == "3":
            quit = True


def generate_password(length):
    letters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k',
               'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T' 'u', 'U',
               'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    password = []
    for i in range(length // 2):
        password.append(letters[random.randint(0, 51)])
    for i in range(length - length // 2):
        password.append(numbers[random.randint(0, 9)])

    print("\n" + ''.join(password))

    clipboard = input("\nWould you like to copy the password to clipboard? (y/n): ")
    if clipboard == "y":
        pyperclip.copy(''.join(password))
        print("\nCopied!")


def main():
    quit = False
    option = ""
    while quit == False:
        print("\n1) Add A Password")
        print("2) Manage Passwords")
        print("3) Password Generator")
        print("4) Exit")

        option = input("\nEnter an option: ")

        if option == "1":
            identity = input("\nEnter the identity of the password: ")
            url = input("Enter the website URL: ")
            username = input("Enter the username: ")
            password = input("Enter the password: ")

            add_password(identity, url, username, password)

        if option == "2":
            manage_passwords()

        if option == "3":
            length = int(input("\nEnter length of password: "))
            generate_password(length)

        if option == "4":
            print("\nQuitting...")
            quit = True


main()
