cost = 1.50
s = 0

while True :
    coin = float(input("Enter coin: "))
    match coin:
        case 0.05 | 0.10 | 0.20 | 0.50 |1.00 :
            s += coin
            if s >= cost  :
                print("Here is your water")
                print("Change: ", s-cost)
                break
        case _ :
            print("Invalid coin")