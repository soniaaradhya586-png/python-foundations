# this didn't work in my laptop for some reason ot kept showing (.venv)
from sayings import hello
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("haello, " + sys.argv[1])

if len(sys.argv) == 2:
    hello(sys.argv[1])
    