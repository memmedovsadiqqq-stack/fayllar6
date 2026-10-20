A = 0
B = 0
C = 0
Spoiled = 0

while True :
    Vote = input("Vote:").upper()
    if Vote == "END":
        break
    elif Vote == "A":
        A += 1
    elif Vote == "B":
        B +=1
    elif Vote == "C":
        C += 1
    else:
        Spoiled +=1
print("A: ", A, "B: ", B,"C: ", C)
print("Spoiled: ",Spoiled)
if A > B and A > C:
    print("Winner: ", "A")
elif B > A and B > C:
    print("Winner: ", "B")
elif C > A and C > B:
    print("Winner: ", "C")
else:
    print("Tie")       