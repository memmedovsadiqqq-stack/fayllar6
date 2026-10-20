free_space = 20

while True :
    command = input().lower()
    if command == "in" :
        free_space -= 1
    elif command == "out":
        free_space += 1
    elif command == "stop":
        break
    else :
        print("Unknown command")
    if free_space == 20 and command == "in":
        print("Garage is full")
    elif free_space == 0 and command == "out":
        print("Garage is empty")