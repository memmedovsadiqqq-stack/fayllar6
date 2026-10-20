PIN = 2580
i = 3
balance = 1000

while True :
    enter_PIN = int(input("Enter PIN: "))
    
    if i > 0:
        if enter_PIN == PIN:
            print("Access granted")
            i = -1
        else:
            i -= 1
            print("Incorrect PIN. You have", i, "attempts left.")
            if i == 0:
                print("Card blocked")
                break
            continue
    while True:
        option = input("Enter option: ")
        match option:
            case "1":
                print("Your balance is", balance)
            case "2":
                amount = int(input("Enter amount to deposit: "))
                if amount > 0:
                    balance += amount
                    print("Your balance is", balance)
                else :
                    print("Invalid amount")
            case "3":
                amount = int(input("Enter amount to withdraw: "))
                if amount > 0 and amount <= balance:
                    balance -= amount
                    print("Your balance is", balance)
                else :
                    print("Invalid amount")
            case "4":
                print("Exiting...")
                break
            case _:
                print("Invalid option")
    break