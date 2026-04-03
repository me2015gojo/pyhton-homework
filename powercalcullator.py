number = int(input("Enter the number: "))
n = int(input("Enter how many powers to calculate: "))
for power in range(1, n + 1):
    result = number ** power
    print(f"{number} ^ {power} = {result}")