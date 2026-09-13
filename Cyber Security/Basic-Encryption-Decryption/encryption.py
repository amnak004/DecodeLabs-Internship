def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


text = input("Enter text: ")
shift = int(input("Enter shift key: "))

encrypted_text = encrypt(text, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("\nOriginal text:", text)
print("Encrypted text:", encrypted_text)
print("Decrypted text:", decrypted_text)