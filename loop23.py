minute = 480
s = 0
while True:
    s += 1
    minute_needed = int(input("Costumer needs (min): "))
    minute -= minute_needed
    if minute <= 0 :
        print("Sorry, come tomorrow")
        break
print("Costumers served: ", s-1)
print("Minutes left: ", minute + minute_needed)