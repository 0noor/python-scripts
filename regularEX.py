import re

pattern = re.compile(r"[a-zA-Z0-9@\$%#]{7,}\d")
pas = input("Enter your password here")
check = pattern.fullmatch(pas)

if check is None:
    print("Password isnt valid")
else:
    print("welcome")
