password = input()
length_ok = len(password) >= 8
special_chars = any(c in "$#!?-_" for c in password)
uppercase_letters = any(c in "ABCD" for c in password)
print(length_ok and special_chars and uppercase_letters)
