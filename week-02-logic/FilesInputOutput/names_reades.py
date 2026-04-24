#with open("names.txt", "r") as file:
#    lines = file.readlines()

#for line in lines:
#    print("hello,", line.rstrip())


# This is more eligent way to represent the same thing as above; but this also has it's ownflaws such like you can't sort the file while using this because it reades line by line
#with open("names.txt", "r") as file:
#    for line in file:
#        print("hello,", line.rstrip())


names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")