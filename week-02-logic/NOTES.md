## Libraries
- libraries are code that other people have written that you canuse in your file
- modules- in python is just a library which has one or more features built inside of it. some of these modules with which python comes in are:
                                           > random
- import keyword in python allows you to import the contents of some functions of a module 
- random.choice(seq) = this function lives in the random module, and seq is used for sequence
- from = is a keyword in python which you can use to import functions from a module; with this keyword you can be a little more specific than import alone
- random.randint(a, b) - this function is used to call a random int between a and b
- random.shuffle(x) = is used to shuffle a list or something
- statistics library = this library also comes with python just like random but this contains functions that are used and are for more statistical in nature
- command-line arguments = this function allows you to arguments that are inputs to the program of just when you are instructing at the command-line
- sys.argv is a variable in sys library = this collects the list of all the words in the prompt that the human typed before hitting the enter: this variable is a list which collects all the words that you type respectively
- sys.exit= this function will help you exit the program then and there i which line it is written
slices= to take a slice of a list is to take a subset of it
example- for arg in sys.argv[1:2]
             code that you want to run
- packages = also known as third party libraries
 one of the websites where you can get these packages is PyPI.org
- pip = it is aprogram that generally comes with python, and allows you to install packages in your mack pc's or any cloud softwere and then you can directly access that package 

## UnitTest
- assert = it is used to boldly claim something is true, but if you assert something in python but it is not true like a boolian expression it will be shown as error
- pytest = it is a third-party program that you can install that will automate your test as long as you write the tests
- packages = packages are a python modules that ate organised inside of a folder; and file __init__ is just a visual representation to python to treat that folder as a package

## FilesInputOutput
- File(I\O) = it is a way to store information in your devices such that they are there when you come back and run them
- open = this function opens a file systematically such that a programmer can reade or write informaiton from that file
example:  file = open("names.txt", "w") here "w"is written to represent that we want to write in that file, we can also use "a" which is used to append 
- with = which in this context allows you to open and close a file
- sorted()= this function in python is used to sort the file in order of alphabets in python and if you want to reverse the arrangement while using sorted go to it's libraies 
- using key in sorted example in students.py we can use key to get a column of a dictionary to be used for sorting 
- lambda function this function is used when you only need to call that function once thus that function has no name, it can be defined as many times as possible but you have to describe what that function will do each and every time. Example in students.py 
- Binary file = a binary file is a file that is just generally zeros and ones that can be laid out in any pattern you want perticularly not in textual information but in graphical information also video information
- pillow library = this library allows you to navigate image file and to perform operations on them.