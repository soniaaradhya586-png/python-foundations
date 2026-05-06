class Student:
    def __init__(self, name, house):
          if not name:
                raise ValueError("Missing name")
          ######if house not in ["Griffindor", "Huffelpuff", "Ravenclaw", "Slytherin"]:
          ######     raise ValueError("Invalid house")
          self.name = name
          self.house = house
          #self.patronus = patronus

    def __str__(self):
          return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
           name = input("Name: ")
           house = input("House: ")
           return cls(name, house)
    
    #@property
    #def name(self):
    #     return self._name
    #
    #@name.setter
    #def name(self, name):
    #     if not name:
    #          raise ValueError("Missing name")
    #     self._name = name

    # Getter
    #@property
    #def house(self):
    #    return self._house
   
    # Setter
    #@house.setter
    #def house(self, house):
    #     if house not in ["Gryffindor", "Huffelpuff", "Ravenclaw", "Slytherin"]:
    #          raise ValueError("Invalid house")
    #     self._house = house   

    #def charm(self):
    #      match self.patronus:
    #           case "Stag":
    #                  return "horse"
    #            case "Otter":
    #                  return "shoe"
    #            case "Jack Russell terrier":
    #                  return "cute dog"
    #                 return "wand"


##def main():
    #name = get_name()
    #house = get_house()
##    student = get_student()
##    print(f"{student[0]} from {student[1]}")


#def get_name():
#        return input("Name: ")

#def get_house():
 #       return input("House: ")

###def main():
###        student =get_student()
        ##if student[0] == "Padma":
        ##     student[1] = "Ravenclaw"
        #print(f"{student[0]} from {student[1]}")
                  #usind dictionarines to change the string
###        if student["name"] == "Padma":
###                student["house"] = "Ravenclaw"
###        print(f"{student['name']} from {student['house']}")


#def get_student():
#        name = input("Name: ")
#        house =  input("House: ")
#        return [name, house]

##def get_student():
##       student = {}
##       student["name"] = input("Name: ")
##       student["house"] = input("House: ")
##       return student

###def get_student():
###       name = input("Name: ")
###       house = input("House: ")
###       return{"name": name, "house": house}

def main():
      student = Student.get()
      print(student)


######def get_student():
     #student = Student
     #student.name = input("Name: ")
     #student.house = input("House: ")
######     name = input("Name: ")
######     house = input("House: ")
     #patronus = input("Patronus: ") 
######     return Student(name, house)

      

if __name__ == "__main__":
     
      #print("Expecto Partonum!")
      #print(student.charm())
     main()