import cowsay
import sys

if len(sys.argv) == 2: #the first element is the name of the file
    cowsay.cow("Hello, " + sys.argv[1])

    cowsay.trex("Hello, " + sys.argv[1])


