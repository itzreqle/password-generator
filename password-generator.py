import os
import random
import string
import argparse
import hashlib
from colorama import init, Fore, Back, Style


init()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--count', type=int, default=1, help='Count for password loop method ( Optional )')
    parser.add_argument('-l', '--length', type=int, default=16, help='Length for password ( Optional )')
    parser.add_argument('-t', '--type', default="all", help='Type for password ( Optional ) [ All / Lower / Upper / Numbers / Symbols ]')
    parser.add_argument('-hp', '--hashpassword', default="false", help='Hashed password ( Optional ) [ True / Flase ]')

    args = parser.parse_args()
    count = args.count
    length = args.length
    type = args.type.lower()
    hash = args.hashpassword.lower()

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = "0123456789"
    symbols = string.punctuation

    if (type == "all"):
        all = lower + upper + numbers + symbols
    elif (type == "lower"):
        all = lower
    elif (type == "upper"):
        all = upper
    elif (type == "numbers"):
        all = numbers
    elif (type == "symbols"):
        all = symbols

    while (len(all) < length):
        all += all

    for _ in range(count):
        password = "".join(random.sample(all, length))
        if (hash == "true"):
            salt = os.urandom(32)
            plaintext = password.encode()

            digest = hashlib.pbkdf2_hmac('sha256', plaintext, salt, 10000)

            hex_hash = digest.hex()

            byte_hash = digest.fromhex(digest.hex())
            print(f"{Fore.BLUE}{password}{Fore.RESET} {Fore.WHITE}{salt.hex()}{Fore.RESET} {Fore.WHITE}{hex_hash}{Fore.RESET}")
        else:
            print(f"{Fore.BLUE}{password}{Fore.RESET}")

if __name__ == "__main__":
    main()
