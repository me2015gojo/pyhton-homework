rows = int(input("How many rows? "))

i = 1
while i <= rows:
    space = 1
    while space <= rows - i:
        print(" ", end="")
        space = space + 1
    
    star = 1
    while star <= i:
        print("*", end="")
        star = star + 1
    
    print()
    i = i + 1