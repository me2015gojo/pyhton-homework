def circumference(radius):
    result = 2 * 22 / 7 * radius
    return result

r = float(input("Enter radius of circle: "))
ans = circumference(r)
print("Circumference of circle:", ans)