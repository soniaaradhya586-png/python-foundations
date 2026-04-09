#x = int (input("wha's x?"))
#y = int (input("what's y?"))

#if x < y:
#    print("x is less than y")
#elif x > y:
#    print("x is greater than y")
#else:                  
 #    print("x is equal to y")



#if x < y or x > y:
 #   print("x is not equal to y")
#else:
 #   print("x is equal to y")


# if x != y:
  #  print("x is not equal to y")
#else:
 #   print("x is equal to y")


name =input("What's your name?")
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
         print("Who?")