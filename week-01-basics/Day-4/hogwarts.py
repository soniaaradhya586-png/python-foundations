#students = ["Harry", "Ron", "Hermione", "Draco", "Neville"]

#for students in students:
#    print(students)

#for i in range(len(students)): 
#    print(i + 1, students[i])

#houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

#students = {
#    "Harry": "Gryffindor",
#    "Hermione": "Gryffindor",
#    "Ron": "Gryffindor",
#   "Neville": "Gryffindor"
#}

#print(students["Harry"])
 
 
#for student in students:
#    print(student, students[student])

students =[
    {"name": "Harry", "house": "Gryffindor", "patronus": "stag"},
    {"name": "Hermione", "house": "Gryffindor", "patronus": "otter"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(f"{{name}} = {student['name']}, {{house}} = {student['house']}, {{patronus}} = {student['patronus']}", sep=", ")