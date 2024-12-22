def check_password_validity(password):
    if len(password) < 6 or len(password) > 16:
        return "Password must be between 6 and 16 characters."

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_characters = "$#@"

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if not has_lower:
        return "Password must contain at least one lowercase letter."
    if not has_upper:
        return "Password must contain at least one uppercase letter."
    if not has_digit:
        return "Password must contain at least one digit."
    if not has_special:
        return "Password must contain at least one special character from [$#@]."

    return "Password is valid."

password = input("Enter a password: ")

result = check_password_validity(password)

print(result)
