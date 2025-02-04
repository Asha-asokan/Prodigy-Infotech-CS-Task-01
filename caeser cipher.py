def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabetic characters as is
    return result
text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))

# Encrypt the text
encrypted_text = caesar_cipher(text, shift)
print(f"Encrypted text: {encrypted_text}")

# Decrypt the text
decrypted_text = caesar_cipher(encrypted_text, -shift)
print(f"Decrypted text: {decrypted_text}")

