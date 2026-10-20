
for floor in range(1, 6):
    if floor != 4:
        print("Floor",floor,":", end=" ")
        for room in range(1, 5): 
            if floor == 4:
                break 
            print(floor * 100 + room, end=" ")
        print()