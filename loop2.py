child_tickets = 0
adult_tickets = 0

for i in range (5):
    age = int(input("Enter your age: "))
    if age < 18 :
        child_tickets = child_tickets + 1
    else :
        adult_tickets = adult_tickets + 1

print(child_tickets)
print(adult_tickets)