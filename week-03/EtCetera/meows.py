#MEOWS = 3
#
#for _ in range(MEOWS):
#    print("meow")

##class Cat:
##    MEOWS = 3
##
##   def meow(self):
##        for _ in range(Cat.MEOWS):
##            print("meow")
##
##cat = Cat()
##cat.meow()

###def meow(n: int) -> None:
###    for _ in range(n):
###        print("meow")

#number: int = int(input("Number: "))
#meow(number)

def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")