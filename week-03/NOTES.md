## Regular Expressions
- regular expressions also known as regexes = is a pattern and it is quite common in programming to mtch a pattern using this we are going to have a new ability to define pattern in our code against the data that we are receaving from someone else
- re library = this library is used to raplace or check different patterns in python
- "." = any character except a newline
- "*" = 0 or more repetitions
- "+" = 1 or more repetition
- "?" = 0 or 1 repetition
- "{m}" = m repetitions
- "{m,n}" = m-n repetitions
- "^" = matches the start of the string
- "$" = matches the end of the string or just before the newline at the end of the string
- "[]" = set of characters 
- "[^]" = complementing the set
- \w = word character ... as well as numbersans the underscore
- \W = not a word character
- \d = decimal digit
- \D = not a decimal digit
- \s = whitespace characters
- \S = not a whitespace character
- "A|B" = either A or B
- (...) = a group
- (?:...) = non-capturing version
- re.match(pattern, string, flags) = this is similar to re.search it just that you dont have to add ^ symbol at the startind it will automatically read the string from the start
- re.fullmarch(pattern, string, flags=0) = in this you dont need to add ^ at the start or $ at the end of the string it automatically does their function for you 
- ":=" = this is officially known as wallrus operator and this allows you to do two things (1) it assigns a value from right to left (2) to assign a boolean expression to that value like if or elif
- re.sub(pattern, repl, string, count=0, flags=0) = this is used for substitution
- re.split(pattern, string, maxsplit=0, flags=0) = this is used for splitting a string for different characters
- re.findall(pattern, string, flags=0) = this allows you to find multiple copies fo same patterns in a string typically more than just one

## Object-Oriented-Programming
- oop = is a type of technique used in python to solve a problem
- tuple = a tuple is a type of data in python that is a collection of type of values(you can't change the values returned using this function)
- calsses = these allow you to create your own data types in python and give them a name
- objects = the class is the def of new data type while the object is the instance of classes
- methods = classes come with methods or functions inside of it that you can define and that will work in a special waty.
- instance method (__init__) = if you want to initializ the contents of a class you define this method
- raise = this is used in python to alert the programmer in the case of somethong went wrong 
- properties = a property is an attribute which you can have more control over just by writing a little more code
- decorators = these are functions that decorate the other functions
- class methods = @classmethod this is another function that you can use specify that this method is not a instance method but rather it is a calss method, it is'nt going to have access to self but it's gonna know which class it is inside of
- note : class should be in your code to typically represent any real world entity
- static mthod = "@staticmethod" 
- inheritance = you can have one class inharit methods or variables from another class in python ar introduce it as an heighercy . sinpaly this means that you can define multiple classes that some how relate to one another

## Exceptions
- try = this ins used in python to literally try something
- except = this is used to define what to do if try dosen't work
- ValueError = refers to an error in the value
- NameError = this refers to that you named a variable that you shouldent
- return = can also be used instead of break to further cut the code. doing so it will automatically break the code while at the same time returning the value
- pass = this function is used when you catch an error that an user can make but you want to let it pass right through

## Et-Cetera
- set = thsi is used to filter out any data that might me duplicated
