m = 0 
s = 0

for i in range (7):
    temp = int(input())
    if temp > 30 :
        s += 1
    if temp > m :
        m = temp
print("Hot days:", s)
print("Hotest day:", m)