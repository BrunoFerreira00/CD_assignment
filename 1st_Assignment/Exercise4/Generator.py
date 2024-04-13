import numpy as np
import pprint

#importing the needed functions already defined in the FMP.py file
import FMP as massProb
# Exercise: 4 . b). i) ii) iii)

# Function to generate N random pins
def generatePin(N):
    pins = []
    for i in range(N):
        # Randomly choose the length of the pin between 4 and 6
        pinLenght = np.random.randint(4, 7)
        # Randomly choose the digits of the pin
        pin = ''.join(np.random.choice(list(FMP_DIGITS.keys()), pinLenght, p=list(FMP_DIGITS.values())))
        pins.append(pin)
    return pins


# Function to generate N random euro million codes
def generateEuroMilCode(N):
    codes = []
    for i in range(N):
        # Set the length of keys and stars since it is fixed
        keyLength = 5
        starLength = 2
        # Randomly choose the key and stars
        key = ' '.join(np.random.choice(list(FMP_EURO_KEY.keys()), keyLength, p=list(FMP_EURO_KEY.values())))
        stars = ' '.join(np.random.choice(list(FMP_EURO_STARS.keys()), starLength, p=list(FMP_EURO_STARS.values())))
        # Concatenate the key and stars
        code = "key " + key + " " + "stars " + stars
        codes.append(code)
    return codes

# Function to generate N random passwords
def generatePassword(N):
    passwords = []
    for i in range(N):
        # Randomly choose the length of the password between 8 and 12
        passwordLength = np.random.randint(8, 13)
        # Randomly choose the characters of the password
        password = ''.join(np.random.choice(list(FMP_CHARS.keys()), passwordLength, p=list(FMP_CHARS.values())))
        passwords.append(password)
    return passwords


FMP_DIGITS = {}
for i in range(10):
    FMP_DIGITS[chr(i)] = 0.1

# Make a for loop to get all 50 keys and 12 stars from euro million
FMP_EURO_KEY = {}
for i in range(1,51):
    FMP_EURO_KEY[str(i)] = 1/50
FMP_EURO_STARS = {}
for i in range(1,13):
    FMP_EURO_STARS[str(i)] = 1/12

# Made a for loop to get all the characters from ASCII table from 33 to 126 since they are the only usable ones
FMP_CHARS = {}
for i in range(33,127):
    FMP_CHARS[chr(i)] = 1/94

# Number of random pins, euro million codes and passwords to generate
N = 50

def main():
    pins = generatePin(N)
    entropy_pin = massProb.calculateEntropy(FMP_DIGITS)
    pprint.pprint(pins)
    print("Entropy:", entropy_pin)
    euro = generateEuroMilCode(N)
    pprint.pprint(euro)
    entropy_euro = massProb.calculateEntropy(FMP_EURO_KEY)
    print("Entropy:", entropy_euro)
    passwords = generatePassword(N)
    pprint.pprint(passwords)
    entropy_password = massProb.calculateEntropy(FMP_CHARS)
    print("Entropy:", entropy_password)

if __name__ == "__main__":
    main()