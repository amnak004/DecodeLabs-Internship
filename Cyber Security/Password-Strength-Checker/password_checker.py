password = input("Enter your password: ")
length = len(password)
has_uppercase = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

if length < 8:
    strength = "Weak"
elif has_uppercase and has_number and has_symbol:
    strength = "Strong"
else:
    strength = "Medium"

print("Password strength: ", strength)
