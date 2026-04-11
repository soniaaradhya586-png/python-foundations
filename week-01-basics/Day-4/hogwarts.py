#students = ["Harry", "Ron", "Hermione", "Draco", "Neville"]

#for students in students:
#    print(students)

#for i in range(len(students)): 
#    print(i + 1, students[i])

#houses = ["Gryffindor", "Gryffindor", "Griffindor", "Slytherin"]

students = {
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Hermione": "Gryffindor",
    "Draco": "Slytherin",
    "Neville": "Gryffindor"
}

#print(students["Harry"]) 

for student in students:
    print(student, students[student])
