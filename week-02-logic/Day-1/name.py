import sys

#try:
#    print("hello, my name is", sys.argv[1])
#xcept IndexError:
#    print("Too few arguments")


if len(sys.argv) < 2:
   sys.exitprint("Too few arguments")
#elif len(sys.argv) > 2:
#    sys.exitprint("Too many arguments")
#   print("Hello, my name is", sys.argv[1])
for arg in sys.argv[1:]:
   print("hello, my name is", arg)
