"""****************************************************************************
*********************************** 1 AULA ***********************************
Vídeos no Bro Code
Estudos: Júlia Tomé de Sousa
#variable = a container for a value. Behaves as the value that it contains
****************************************************************************"""

#string = a series of characters
first_name = "Bro"
last_name = "Code"
full_name = first_name +" "+ last_name
print("Hello "+full_name)
# print(type(first_name))

#int = a whole integer
age = 21
age += 1
print("Your age is: "+str(age))
# print(type(age))

#float = a decimal number
height = 250.5
print("Your height is: "+str(height)+"cm")
# print(type(height))

#boolean = True or False
human = True
print("Are you a human: "+str(human))
# print(type(human))

print("""****************************************************************************
***********************************  2 AULA ********************************
****************************************************************************""")
# multiple assignment = allows us to assign multiple variables at the same time in one line of code

name = "Bro"
age = 21
attractive = True

name, age, attractive = "Bro", 21, True

print(name)
print(age)
print(attractive)

# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30

# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)

print("""****************************************************************************
***********************************  3 AULA ********************************
****************************************************************************""")
name = "Bro"

print(len(name)) #technically this is a function
print(name.find("o"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o","a"))
print(name*3)

print("""****************************************************************************
***********************************  4 AULA: Python type cast **************
****************************************************************************""")
#type casting = convert the data type of a value to another data type.

x = 1   #int
y = 2.0 #float
z = "3" #str

x = int(x)
y = int(y)
z = int(z)
print(x)
print(y)
print(z*3)

x = float(x)
y = float(y)
z = float(z)
print(x)
print(y)
print(z*3)

x = str(x)
y = str(y)
z = str(z)
print(x)
print(y)
print(z*3)

print("""****************************************************************************
**************************  5 AULA: Python user input  *********************
****************************************************************************""")
#name = input("What is your name?: ")
#age = int(input("How old are you?: "))
#height = float(input("How tall are you?: "))
name = "Julia"
age = 24
height = 155 

print("Hello "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+"cm tall")

print("""****************************************************************************
**************************  6 AULA: Python math functions ******************
****************************************************************************""")
import math

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi)) #3
print(math.ceil(pi)) #4
print(math.floor(pi)) #3
print(abs(pi)) #3.14
print(pow(pi,2)) #9.8596
print(math.sqrt(pi)) #1.772004514666935
print(max(x,y,z)) #3
print(min(x,y,z)) #1

print("""****************************************************************************
**************************  7 AULA: Python string slicing ******************
****************************************************************************""")
# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Bro Code"

first_name = name[:3]       # [0:3]
last_name = name[4:]        # [4:end]
funky_name = name[::2]      # [0:end:2]
reversed_name = name[::-1]  # [0:end:-1]

print("First Name "+ first_name) #Bro
print(last_name) #Code
print(funky_name) #BoCd
print(reversed_name) #edoC orB

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) #o direito é da direita pra esquerda

print(website1[slice]) #google
print(website2[slice]) #wikipedia

print("""****************************************************************************
**************************  8 AULA: Python if statements *******************
****************************************************************************""")
# if statement = a block of code that will execute if it's condition is true

#age = int(input("How old are you?: "))
age = 22

if age == 100:
    print("You are a century old!")
elif age >= 18:
    print("You are an adult!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You are a child!")

print("""****************************************************************************
**************************  9 AULA: Python logical operators ***************
****************************************************************************""")
# logical operators (and,or,not) = used to check if two or more conditional statements is true

#temp = int(input("What is the temperature outside?: "))
temp = 22

if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad today!")
    print("stay inside!")
    
print("""****************************************************************************
**************************  10 AULA: Python while loop *********************
****************************************************************************""")
# while loop =  a statement that will execute it's block of code,
#                        as long as it's condition remains true

name = ""

while len(name) == 0:
    name = "Julia"
    #name = input("Enter your name: ")

print("Hello "+name)

print("""****************************************************************************
**************************  11 AULA: Python for loop ***********************
****************************************************************************""")
# for loop =    a statement that will execute it's block of code
#                      a limited amount of times
#
#                     while loop = unlimited
#                     for loop = limited

import time

#for i in range(10):
    #print(i+1)

#for i in range(50,100+1,2):
    #print(i)

#for i in "Bro Code":
    #print(i)

for seconds in range(5,0,-1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!")

print("""****************************************************************************
**************************  12 AULA: Python nested loops *******************
****************************************************************************""")
#python #nested #loops

# nested loops =    The "inner loop" will finish all of it's iterations before
#                   finishing one iteration of the "outer loop"

#rows = int(input("How many rows?: "))
#columns = int(input("How many columns?: "))
#symbol = input("Enter a symbol to use: ")
rows = 4
columns = 4
symbol = "@"

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
    
print("""****************************************************************************
**************************  13 AULA: Python break continue pass ************
****************************************************************************""")
# Loop Control Statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop.
# pass =        does nothing, acts as a placeholder

while True:
    #name = input("Enter your name: ")
    name = "Julia"
    if name != "":
        break

phone_number = "123-456-7890"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
        
print("""****************************************************************************
**************************  14 AULA: Python lists **************************
****************************************************************************""")
# list = used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti","pudding"]

food[0] = "sushi"

food.append("ice cream")
print(food) #['sushi', 'hamburger', 'hotdog', 'spaghetti', 'pudding', 'ice cream']
food.remove("hotdog")
print(food) #['sushi', 'hamburger', 'spaghetti', 'pudding', 'ice cream']
food.pop()
print(food) #['sushi', 'hamburger', 'spaghetti', 'pudding']
food.insert(0,"cake")
print(food) #['cake', 'sushi', 'hamburger', 'spaghetti', 'pudding']
food.sort()
print(food) #['cake', 'hamburger', 'pudding', 'spaghetti', 'sushi']
#food.clear()
print(food) #[]

for x in food:
    print(x)    #cake
                #hamburger
                #pudding
                #spaghetti
                #sushi
    
print("""****************************************************************************
**************************  15 AULA: Python 2D lists ************************
****************************************************************************""")
# 2D lists = a list of lists

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks,dinner,dessert]
print(food) #[['coffee', 'soda', 'tea'], ['pizza', 'hamburger', 'hotdog'], ['cake', 'ice cream']]
print(food[0][0])

print("""****************************************************************************
**************************  16 AULA: Python tuples *************************
****************************************************************************""")
# tuple =   collection which is ordered and unchangeable
#                used to group together related data

student = ("Bro",21,"male")

print(student.count("Bro")) #1
print(student.index("male")) #2

for x in student:
    print(x) #Bro #21 #Male

if "Bro" in student:
    print("Bro is here!")
    
print("""****************************************************************************
**************************  17 AULA: Python sets ***************************
****************************************************************************""")
# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin")
print(utensils) #{'fork', 'napkin', 'spoon', 'knife'}
utensils.remove("fork") 
#utensils.clear()
print(utensils) #{'napkin', 'spoon', 'knife'}
dishes.update(utensils)
print(dishes) #{'plate', 'napkin', 'spoon', 'bowl', 'cup', 'knife'}
dinner_table = utensils.union(dishes)
print(dinner_table) #{'plate', 'spoon', 'knife', 'cup', 'napkin', 'bowl'}

print(dishes.difference(utensils)) #{'plate', 'bowl', 'cup'}
print(utensils.intersection(dishes)) #{'plate', 'bowl', 'cup'}

for x in utensils:
    print(x)
    
print("""****************************************************************************
**************************  18 AULA: Python dictionaries ********************
****************************************************************************""")
#dictionary =  A changeable, unordered collection of unique key:value pairs
#                      Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'})
print(capitals) #{'USA': 'Washington DC', 'India': 'New Dehli', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}
capitals.update({'USA':'Las Vegas'})
print(capitals) #{'USA': 'Las Vegas', 'India': 'New Dehli', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}
capitals.pop('China')
print(capitals) #{'USA': 'Las Vegas', 'India': 'New Dehli', 'Russia': 'Moscow', 'Germany': 'Berlin'}
#capitals.clear()

print(capitals['Germany']) #Berlin
print(capitals.get('Germany')) #Berlin
print(capitals.keys()) #dict_keys(['USA', 'India', 'Russia', 'Germany'])
print(capitals.values()) #dict_values(['Las Vegas', 'New Dehli', 'Moscow', 'Berlin'])
print(capitals.items()) #dict_items([('USA', 'Las Vegas'), ('India', 'New Dehli'), ('Russia', 'Moscow'), ('Germany', 'Berlin')])

for key,value in capitals.items():
    print(key, value)
    
print("""****************************************************************************
**************************  19 AULA: Python indexing ************************
****************************************************************************""")
#python #index #indexing
# index operator [] = gives access to a sequence’s element (str,list,tuples)

name = "bro Code!"

#if(name[0].islower()):
   #name = name.capitalize()
  
first_name = name[:3].upper()
last_name = name[4:].lower()
last_character = name[-1]

print(first_name) #BRO
print(last_name) #code!
print(last_character) #!

print("""****************************************************************************
**************************  20 AULA: Python functions ***********************
****************************************************************************""")
# function = a block of code which is executed only when it is called.

def hello(first_name,last_name,age):
    print("hello "+first_name+" "+last_name) #hello Bro Code
    print("You are "+str(age)+" years old") #You are 21 years old
    print("Have a nice day!") 

hello("Bro","Code",21)

print("""****************************************************************************
**************************  21 AULA: Python return statement ***************
****************************************************************************""")
#return statement = Functions send Python values/objects back to the caller.
#                    These values/objects are known as the function’s return value

def multiply(number1,number2):
    return number1 * number2

x = multiply(6,8)

print(x) #48

print("""****************************************************************************
**************************  22 AULA: Python keyword arguments **************
****************************************************************************""")
# keyword arguments =   arguments preceded by an identifier when we pass them to a function
#                       The order of the arguments doesn't matter, unlike positional arguments
#                       Python knows the names of the arguments that a function receives

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)


hello(last="Code",middle="Dude",first="Bro") #Hello Bro Dude Code

print("""****************************************************************************
**************************  23 AULA: Python nested function calls  *********
****************************************************************************""")
# nested functions calls =  function calls inside other function calls
#                           innermost function calls are resolved first
#                           returned value is used as argument for the next outer function

#num = input("Enter a whole positive number: ")
num = -3.14
num = float(num)
num = abs(num)
num = round(num)
print(num) #3

#print(round(abs(float(input("Enter a whole positive number: ")))))
print(round(abs(float(num))))  #3

print("""****************************************************************************
**************************  24 AULA: Python variable scope *****************
****************************************************************************""")
# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped version of a variable can be created

name = "Bro" # global scope (available inside & outside functions)

def display_name():
    name = "Code"    # local scope (available only inside this function)
    print(name) #Code


display_name()
print(name) #Bro

print("""****************************************************************************
**************************  25 AULA: Python *args **************************
****************************************************************************""")
# *args =   parameter that will pack all arguments into a tuple
#                useful so that a function can accept a varying amount of arguments

def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum #36


print(add(1,2,3,4,5,6,7,8))

print("""****************************************************************************
**************************  26 AULA: Python **kwargs ***********************
****************************************************************************""")
# **kwargs =   parameter that will pack all arguments into a dictionary
#                       useful so that a function can accept a varying amount of keyword arguments

def hello(**kwargs):
    #print("Hello " + kwargs['first'] + " " + kwargs['last'])
    print("Hello",end=" ")
    for key,value in kwargs.items():
        print(value,end=" ") #Hello Mr. Bro Dude Code


hello(title="Mr.",first="Bro",middle="Dude",last="Code") 

print("""****************************************************************************
**************************  27 AULA: Python string format ******************
****************************************************************************""")
# str.format() =    optional method that gives users
#                   more control when displaying output

animal = "cow"
item = "moon"

print("The "+animal+" jumped over the "+item) #The cow jumped over the moon

# {} = format field
print("The {} jumped over the {}".format("cow","moon")) #The cow jumped over the moon
print("The {0} jumped over the {1}".format(animal,item)) # positional arguments
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))   # keyword arguments

text = "The {} jumped over the {}"
print(text.format("cow","moon"))

name = "Bro"

print("My name is {}".format(name)) #My name is Bro
print("My name is {:10}".format(name,name))   # amount of padding
print("My name is {:<10}".format(name,name))  # < = left align
print("My name is {:>10}".format(name,name))  # > = right align #My name is        Bro
print("My name is {:^10}".format(name,name))  # ^ = center align #My name is    Bro  


# str.format() =    optional method that gives users
#                   more control when displaying output

number = 1000

print("The number pi is {:.3f}".format(number)) #The number pi is 1000.000
print("The number is {:,}".format(number)) #The number is 1,000
print("The number is {:b}".format(number)) #The number is 1111101000
print("The number is {:o}".format(number)) #The number is 1750
print("The number is {:X}".format(number)) #The number is 3E8
print("The number is {:E}".format(number)) #The number is 1.000000E+03

print("""****************************************************************************
**************************  28 AULA: Python random numbers *****************
****************************************************************************""")
import random

x = random.randint(1,6)
y = random.random()

myList = ['rock','paper','scissors']
z = random.choice(myList)

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]

random.shuffle(cards)

print(cards) #['J', 8, 2, 'K', 6, 9, 1, 5, 4, 7, 'A', 3, 'Q']

print("""****************************************************************************
**************************  29 AULA: Python exception handling *************
****************************************************************************""")
# exception =   events detected during execution that interrupt the flow of a program

try:
    #numerator = int(input("Enter a number to divide: "))
    numerator = 22
    #denominator = int(input("Enter a number to divide by: "))
    denominator = 23
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result) #0.9565217391304348
finally:
    print("This will always execute")
    
print("""****************************************************************************
**************************  30 AULA: Python file detection ******************
****************************************************************************""")
import os

path = "C:\\Users\\User\\Desktop\\test.txt"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist!")
    
print("""****************************************************************************
**************************  31 AULA: Python read a file  ********************
****************************************************************************""")
try:
    with open('test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")
    
print("""****************************************************************************
**************************  32 AULA: Python write a file ********************
****************************************************************************""")
text = "Yooooooooo\nThis is some text\nHave a good one!\n"

with open('test.txt','w') as file:
    file.write(text)
    
print("""****************************************************************************
**************************  33 AULA: Python copy a file  ********************
****************************************************************************""")
# copyfile() =  copies contents of a file
# copy() =       copyfile() + permission mode + destination can be a directory
# copy2() =     copy() + copies metadata (file’s creation and modification times)

import shutil

shutil.copyfile('test.txt','copy.txt') #src,dst

print("""****************************************************************************
**************************  34 AULA: Python move a file **********************
****************************************************************************""")
import os

source = "C:\\Users\\User\\Desktop\\source.txt"
destination = "C:\\Users\\User\\Desktop\\destination.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")
    
print("""****************************************************************************
**************************  35 AULA: Python delete a file ******************
****************************************************************************""")
import os
import shutil

path = "test.txt"

try:
    os.remove(path)    #delete a file
    #os.rmdir(path)     #delete an empty directory
    #shutil.rmtree(path)#delete a directory containing files
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")
    
print("""****************************************************************************
**************************  36 AULA: Python rock, paper, scissors game *****
****************************************************************************""")
"""
import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    elif player == "paper":
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win!")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")
"""
print("""****************************************************************************
**************************  37 AULA: Python quiz game **********************
****************************************************************************""")
"""
def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")
"""
print("""****************************************************************************
************  38 AULA: Python Object Oriented Programming in 10 minutes ****
****************************************************************************""")
"""
from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.drive()
car_2.stop()
#------------------------------------------------------------------
class Car:

    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")
"""
print("""****************************************************************************
**************************  39 AULA: Python class variables ****************
****************************************************************************""")
"""
from car import Car

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

#Car.wheels = 2

print(car_1.wheels)
print(car_2.wheels)
#---------------------------------------------------------------------
class Car:

    wheels = 4 #class variable

    def __init__(self,make,model,year,color):
        self.make = make    #instance variable
        self.model = model  #instance variable
        self.year = year    #instance variable
        self.color = color  #instance variable
"""        
print("""****************************************************************************
**************************  39 AULA: Python inheritance ********************
****************************************************************************""")
class Animal:

    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")

class Rabbit(Animal):

    def run(self):
        print("This rabbit is running")

class Fish(Animal):

    def swim(self):
        print("This fish is swimming")

class Hawk(Animal):

    def fly(self):
        print("This hawk is flying")


rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive)
fish.eat()
hawk.sleep()

rabbit.run()
fish.swim()
hawk.fly()

print("""****************************************************************************
**************************  40 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  41 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  42 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  43 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  44 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  45 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  46 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  47 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  48 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  49 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  50 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  51 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  52 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  53 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  54 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  55 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  56 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  57 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  58 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  59 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  60 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  61 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  62 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  63 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  64 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  65 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  66 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  67 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  68 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  69 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  70 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  71 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  72 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  73 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  74 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  75 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  76 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  77 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  78 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  79 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  80 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  81 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  82 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  83 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  84 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  85 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  86 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  87 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  88 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  89 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  90 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  91 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  92 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  93 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  94 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  95 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  96 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  97 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  98 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  99 AULA: Python inheritance ********************
****************************************************************************""")

print("""****************************************************************************
**************************  100 AULA: Python inheritance ********************
****************************************************************************""")
