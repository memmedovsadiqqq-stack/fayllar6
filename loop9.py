balance = 500

while balance == 500:
    amount = int(input())
    if amount == 0 :
        print("Goodbye")
        break
    elif amount < 0:
        print("Invalid amount")
        continue
    elif amount > balance:
        print("Insufficient balance")
        continue
    else :
        balance -= amount
        print("Balance:" ,balance)
        print("Amount:" ,amount)