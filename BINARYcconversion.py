
decimal = int(input("Enter a decimal number: "))


if decimal == 0:
    binary = "0"

else:
    binary = "" 
    num = decimal  
    

    while num > 0:
        remainder = num % 2           
        binary = str(remainder) + binary  
        num = num // 2                

print("Decimal number is:", decimal)
print("Binary number is:", binary)