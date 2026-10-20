while True :
    password = input()
    if len(password) < 8:
        print("Weak password: too short")
    elif password.isdigit():
        print("Weak password: no letters")
    elif password.islower():
        print("Weak password: no uppercase letters")
    else:
        print("Strong password")
        break