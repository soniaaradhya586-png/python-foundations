##students = [
##   {"name": "Harry", "house": "Gryffindor"},
##    {"name": "Ron", "house": "Gryffindor"},
##    {"name": "Hermione", "house": "Gryffindor"},
##    {"name": "Draco", "house": "Slytherin"},
##]

#gryffindor = [
#    student["name"] for student in students if student["house"] == "Gryffindor"
#]
#
#for gryffindor in sorted(gryffindor):
#    print(gryffindor)

##def is_gryffindor(s):
##    return s["house"] == "Gryffindor"
##
##gryffindors = filter(is_gryffindor, students)
##
##for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
##                        print(gryffindor["name"])

###students =["Hermione", "Harry", "Ron"]
####gryffindors = []
###
####for student in students:
####    gryffindors.append({"name": student, "house": "gryffindor"})
###
####gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
###
###gryffindors = {student: "Gryffindor" for student in students}
###
###print(gryffindors)

students = ["Hermione", "Harry", "Ron"]

#for i in range(len(students)):
#    print(i + 1, students[1])

for i, student in enumerate(students):
    print(i + 1, student)

