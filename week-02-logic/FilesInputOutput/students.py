import csv


#with open("students.csv") as file:
#    for line in file:
#        row = line.rstrip().split(",")
#        print(f"Name: {row[0]}, House: {row[1]}")

####students = []

####with open("students.csv") as file:
####    for line in file:
####        name, house = line.rstrip().split(",")
       # students.append(f"{name} is in {house}")
        ##student = {}
        ##student["name"] = name
        ##student["house"] = house
        ### same thing as above can be achived just by doing this 
####        student = {"name": name, "house": house}
####        students.append(student)

#for students in sorted(students):
#    print(students)


#def get_name(student):
#    return student["name"]


#####students = []

#####with open("students.csv") as file:
#####    reader = csv.reader(file)
#####    for name, home in reader:
#####        students.append({"name": name, "home": home})


#####for student in sorted(students, key= lambda student: student["name"]):
#####    print(f"{student['name']} is from {student['home']}")

name = input("What's your name? ")
home = input("Where's your house? ")

with open("students.csv", "a", newline="") as file:
    #writer = csv.writer(file)
    #writer.writerow([name, home])
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
    