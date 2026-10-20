username_main = "admin"
password_main = 1234

for i in range(3):
    username = input()
    password = int(input())

    if username == username_main and password == password_main:
        print("welcome")
        break
    else:
        print("wrong username or password")