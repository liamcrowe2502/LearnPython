def myFunction(names):
    print(names)

myFunction("Liam")

#Unknown parameters begin with *
def myFunction1(*names):
    print(names[1])

myFunction1("Liam", "Crowe")

def myFunction2(fruits):
    for x in fruits:
        print(x)
fruits = ["apple", "banana", "cherry"]
myFunction2(fruits)

def myFunction3(x):
    return 5*x

print(myFunction3(3))
