#with open("students.csv") as file:
#    for line in file:
#        row = line.rstrip().split(",")
#        print(f"Name: {row[0]}, House: {row[1]}")

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
       # students.append(f"{name} is in {house}")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

#for students in sorted(students):
#    print(students)

for student in students:
    print(f"{student['name']} is in {student['house']}")