def square_odd_even(start, end):
    squares = []
    for num in range(start, end + 1):
        squares.append(num * num)
    
    odd_squares = []
    even_squares = []
    
    for sq in squares:
        if sq % 2 == 0:
            even_squares.append(sq)
        else:
            odd_squares.append(sq)
    
    print(even_squares)
    print(odd_squares)

a = int(input())
b = int(input())
square_odd_even(a, b)