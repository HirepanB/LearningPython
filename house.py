name = input("What's your name? ")

if name == "Harry" :
    print("Gryffindor")
elif name == "Hermione":
    print("Gryffindor")
elif name == "Ron":
    print("Draco")
else:
    print("Who?")


## version 2
name = input("What's your name? ")

if name == "Harry"  or name == "Hermion" or name == "Ron":
    print("Gryffindor")
elif name == "Ron":
    print("Draco")
else:
    print("Who?")

## version 3
name = input("What's your name? ")

match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
    

## version 3
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
    
