num = int(input("Enter a number: ")) #1st one
odd_numbers = [x for x in range(num) if x % 2 != 0]
even_numbers = [x for x in range(num) if x % 2 == 0]
print(odd_numbers)
print(even_numbers)

fruits = ["apple", "banana", "mango", "orange"] #2nd one
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print(fruits)
print(capitalized_fruits)