s = 0
k = 50
month = 0

while True :
    month += 1
    s += k
    k += 10
    if s >= 1000 :
        print("Month", month,":", s)
        break
    else :
        print("Month", month,":", s)