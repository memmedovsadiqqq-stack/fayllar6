n = 1

while n > 0:
    passowrd = input()
    if len(passowrd) >= 8:
        print("Password i accepted")
        break
    else:
        print("Too short, try again")