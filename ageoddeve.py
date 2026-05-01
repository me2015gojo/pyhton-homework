try:
    age = int(input("Enter your age: "))
    
    if age < 0:
        print("Value Error: Age cannot be negative")
    elif age % 2 == 0:
        print("Even")
    else:
        print("Odd")

except ValueError:
    print("Value Error: Enter a whole number")