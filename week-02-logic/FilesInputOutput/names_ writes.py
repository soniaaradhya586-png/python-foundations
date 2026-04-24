#names =[]

#for _ in range(3):
     #name = input("What's your name? ")
 #    names.append(input("What's your name? "))

#for name in sorted(names):
 #    print(f"hello, {name}")
name = input("What's your name? ")

with open("names.txt", "a") as file:
     file.write(f"{name}\n")
#file.close()
