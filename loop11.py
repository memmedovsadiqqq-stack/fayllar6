results = 0
passed = 0
failed = 0
grade = 0
i = 0
m = 0

while True :
    grade = int(input()) 
    if grade > m :
        m = grade
    if grade >= 51 and grade <= 100:
        passed += 1
    elif grade < 51 and grade != -1 and grade > -1:
        failed += 1
        
    elif grade == -1:
        break
    else :
        print("Invalid number")
        continue
    results += grade
    i += 1
print("Passed:", passed)
print("Failed:", failed)
print("Highest:", m)
print("Average:", results/i)