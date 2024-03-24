"""
Importing the modules:
     - Generator since theres a function that generates passwords
     - gzip to compress the file
     - os to be able to get the size in bytes of the files
"""
import Generator
import gzip
import os

def main():
    # Number of passwords to generate
    N = 1000
    passwords = Generator.generatePassword(N)
    # Write the passwords to a .txt file
    with open("passwords.txt", "w") as file:
        for password in passwords:
            file.write(password + "\n")
    # Compress the file
    with open("passwords.txt", "rb") as file:
        with gzip.open("passwords.txt.gz", "wb") as file_gz:
            file_gz.writelines(file)
    # Get the size of the original and compressed file
    original_size = os.path.getsize("passwords.txt")
    compressed_size = os.path.getsize("passwords.txt.gz")
    # Calculate the difference
    difference = original_size - compressed_size
    print("Original size: ", original_size, "bytes, compressed size: ", compressed_size, "bytes, difference: ", difference , "bytes")

if __name__ == "__main__":
    main()