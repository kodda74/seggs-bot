from time import sleep

print("What is your name?")

name = input("enter here: ")

print("Do u wanna know how to seggs?")

answ = input("enter here: ")

def printBees():
    a_file = open("script.txt")

    lines = a_file.readlines()
    for line in lines:
        sleep(0.1)
        print(line)

if answ == "yes":
    print('Too bad have the bee movie script instead')

    sleep(1)

    printBees()

else:
    print("Too bad have bee movie script anyway")

    sleep(1)

    printBees()


