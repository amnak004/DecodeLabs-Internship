def check_password(password):

    length = len(password)

    has_uppercase = any(char.isupper() for char in password)
    has_number = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    suggestions = []
    common_passwords = ["password", "123456", "12345678", "qwerty", "admin"]
    is_common = password.lower() in common_passwords

    if length < 8 or is_common:
        strength = "Weak"
        if length < 8:
            suggestions.append("Use at least 8 characters.")
        if is_common:
            suggestions.append("Avoid using common passwords.")

    elif has_uppercase and has_number and has_symbol:
        strength = "Strong"
    else:
        strength = "Medium"
        if not has_uppercase:
            suggestions.append("Add at least one uppercase letter.")
        if not has_number:
            suggestions.append("Add at least one number.")
        if not has_symbol:
            suggestions.append("Add at least one special character.")
    return strength, suggestions

password = input("Enter your password: ")
strength, suggestions = check_password(password)

print("Password strength: ", strength)
if suggestions:
    print("Suggestions: ")
    for suggestion in suggestions:
        print("-",suggestion)
