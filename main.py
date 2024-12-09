#!/bin/python3
import math
import getpass
import re

def too_common(password) -> bool:
    try:
        wordlist = '/usr/share/wordlists/rockyou.txt'
        words = re.findall('\w+', open(wordlist, encoding='latin-1').read().lower())
    except Exception as e:
        print("\nCouldn't find wordlist. Ignoring...")
        print("Please note that this will decrease entropy precision.")
        print("Consider defining a valid wordlist in the script.")

        return False

    if password in words:
        return True
    else:
        return False
        

def get_possible_symbols(password) -> int:
    lowercase = 0
    uppercase = 0
    numbers = 0
    special = 0
    
    for i in password:
        if re.match('[a-z]', i):
            lowercase = 26
        elif re.match('[A-Z]', i):
            uppercase = 26
        elif re.match('[0-9]', i):
            numbers = 10
        else:
            special = 23
        
    return lowercase + uppercase + numbers + special


def calculate_entropy(password) -> int:
    if too_common(password):
        return 0

    L = len(password)
    S = get_possible_symbols(password)
    SL = S**L
    entropy = math.log2(SL)
    
    return int(entropy)


def show_result(entropy) -> str:
    appreciations = [
        (0, 35, 'very weak'),
        (36, 59, 'weak'),
        (60, 119, 'strong'),
        (120, float('inf'), 'very strong')
    ]

    result = f'\nEntropy is {entropy} bits\n'
    
    if entropy == 0:
        result += "Your password is too common!"
    else:
        for lower, upper, appreciation in appreciations:
            if lower <= entropy <= upper:
                result += f'Your password is {appreciation}'
                break

    if(entropy < 60):
        result += '\n\n[!] Follow these tips to increase your password!'
        result += '\n[!] https://www.cisa.gov/secure-our-world/use-strong-passwords'
    
    print(result)


def main():
    print('Password entropy analysis')
    password = getpass.getpass('Input:')
    
    entropy = calculate_entropy(password)
    show_result(entropy)


if __name__ == '__main__':
    main()
