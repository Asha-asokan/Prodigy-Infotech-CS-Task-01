# Prodigy-Infotech-CS-Task-01

This is a simple Python implementation of the Caesar cipher, which can be used for both encryption and decryption of messages. The program allows you to input a message, choose a shift value, and select whether you want to encrypt or decrypt the message using the Caesar cipher technique.

# Features
- Encryption: Shift each letter in the message by a specified number of positions down the alphabet.
- Decryption: Reverse the shift to get the original message.
- Handles both uppercase and lowercase letters.
- Non-alphabetic characters (spaces, punctuation, numbers, etc.) remain unchanged.
- Interactive command-line interface.

# How it Works
The Caesar cipher works by shifting the letters of the alphabet by a certain number. For example, with a shift of 3:

- 'A' becomes 'D'
- 'B' becomes 'E'
- 'Z' becomes 'C'
For decryption, the program shifts the letters in the opposite direction, effectively undoing the encryption.

# Getting Started
- Prerequisites
To run the program, you need to have Python installed on your computer. The code is written in Python 3.x, so make sure you have Python 3 installed. You can check if Python is installed by running:
python --version
or
python3 --version

# Running the Program
- Clone or download this repository to your local machine.
- Open a terminal and navigate to the folder where you have saved the project files.
- Run the following command to start the program:
python caesar_cipher.py
or
python3 caesar_cipher.py
- The program will display an interactive menu where you can choose whether to encrypt or decrypt a message.

# Example Usage
# - Encryption:

- Message: hello
- Shift value: 3
- Action: encrypt
- Encrypted message: khoor

 # - Decryption:
- Message: khoor
- Shift value: 3
- Action: decrypt
- Decrypted message: hello
