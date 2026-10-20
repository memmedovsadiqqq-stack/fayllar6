card = input()
s = 0

while True:
    if card.isdigit() and len(card)==16:
        n = list(card)
        for i in range (1,len(n),2):
            s = s + int(n[i])
        for i in range (0,len(n),2):
            k = int(n[i])  * 2
            if k > 9:
                k -= 9
            s += k
        break
    elif len(card) < 16:
        print("Must be 16 digits")
        break
    else:
        print("Only numbers")
        break
if s % 10 == 0:
    print("Valid card number")
else:
    print("Invalid card number")