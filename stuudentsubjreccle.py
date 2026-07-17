student = {"name": "Rose", "age": 20, "course": "CS"}

print(student["name"])
print(student.get("age"))

student["grade"] = "A"
student["age"] = 21

student["marks"] = {"math": 90, "python": 95}
student["marks"]["math"] = 100

student.pop("course")

print(len(student))

for key, value in student.items():
    print(key, value)