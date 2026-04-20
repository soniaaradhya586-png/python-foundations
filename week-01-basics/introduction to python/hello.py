# Ask user for their name, you can also add .strip at the end of this line to make the code short
#name = input("What is your name? ")

# Remove Whitespace from str, note- you can update values inside a variable just by using assignment operator again and again.
#you can also chain these
#name = name.strip().title().capitalize()

#Capatalise user's name
#name = name.capitalize()    
#name = name.title()

#print(f"Hello, \"{name}!\"", end=" ") 

# split user's name into first and last name, and print them separately
#first , last = name.split(" ")
#print(f"hello {first}")

# def for defining a function
# scope reffers to a variable only existing in the context in which you defined it 

def hello(to):
    print("Hello,", to)
    

name = input ("What's your name?")
hello(name)