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
**************************  40 AULA: Python multilevel inheritance  ********
****************************************************************************""")
class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):

    def bark(self):
        print("This dog is barking")


dog = Dog()
print(dog.alive)    # inherited from the Organism class
dog.eat()           # inherited from the Animal class
dog.bark()          # defined in Dog class


print("""****************************************************************************
**************************  40 AULA: Python multilevel inheritance  ********
****************************************************************************""")
# multiple inheritance = when a child class is derived from more than one parent class

class Prey:

    def flee(self):
        print("This animal flees")

class Predator:

    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass


rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# rabbit.flee()
# hawk.hunt()
fish.flee()
fish.hunt()

print("""****************************************************************************
**************************  42 AULA: Python method overriding **************
****************************************************************************""")
class Animal:
    
    #overriden method
    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    
    #overriding method
    def eat(self):
        print("This rabbit is eating a carrot")


rabbit = Rabbit()
rabbit.eat()

print("""****************************************************************************
**************************  43 AULA: Python method chaining ****************
****************************************************************************""")
# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

    def turn_on(self):
        print("You start the engine")
        return self

    def drive(self):
        print("You drive the car")
        return self

    def brake(self):
        print("You step on the brakes")
        return self

    def turn_off(self):
        print("You turn off the engine")
        return self


car = Car()

# car.turn_on().drive()
# car.brake().turn_off()
# car.turn_on().drive().brake().turn_off()

car.turn_on()\
    .drive()\
    .brake()\
    .turn_off()
    
print("""****************************************************************************
**************************  44 AULA: Python super function *****************
****************************************************************************""")
# super() = Function used to give access to the methods of a parent class.
#                  Returns a temporary object of a parent class when used

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):

    def __init__(self, length, width):

        super().__init__(length,width)

    def area(self):
        return self.length*self.width

class Cube(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height


square = Square(3, 3)
cube = Cube(3, 3, 3)

print(square.area())
print(cube.volume())

print("""****************************************************************************
**************************  45 AULA: Python abstract classes ***************
****************************************************************************""")
# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods.
# abstract method = a method that has a declaration but does not have an implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print("You drive the car")

    def stop(self):
        print("This car is stopped")

class Motorcycle(Vehicle):

    def go(self):
        print("You ride the motorcycle")

    def stop(self):
        print("This motorcycle is stopped")


#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

#vehicle.stop()
car.stop()
motorcycle.stop()


print("""****************************************************************************
**************************  46 AULA: Python objects as arguments ***********
****************************************************************************""")
class Car:

    color = None

class Motorcycle:

    color = None

def change_color(vehicle,color):

    vehicle.color = color


car_1 = Car()
car_2 = Car()
car_3 = Car()

bike_1 = Motorcycle()

change_color(car_1,"red")
change_color(car_2,"white")
change_color(car_3,"blue")
change_color(bike_1,"black")

print(car_1.color)
print(car_2.color)
print(car_3.color)
print(bike_1.color)

print("""****************************************************************************
**************************  47 AULA: Python duck typing ********************
****************************************************************************""")
# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("This duck is qwuacking")

class Chicken:

    def walk(self):
        print("This chicken is walking")

    def talk(self):
        print("This chicken is clucking")

class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("You caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)

print("""****************************************************************************
**************************  48 AULA: Python walrus operator :=  ************
****************************************************************************""")
# walrus operator :=
# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# happy = True
# print(happy)

# print(happy := True)

# foods = list()
# while True:
#   food = input("What food do you like?: ")
#       if food == "quit":
#           break
#   foods.append(food)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)
    
print("""****************************************************************************
**************************  49 AULA: Python assign functions to variables **
****************************************************************************""")
def hello():
    print("Hello")


hi = hello
hi()

# say = print
# say("Whoa! I can't believe this works! :O")

print("""****************************************************************************
**************************  50 AULA: Python higher order functions  ********
****************************************************************************""")
#  Higher Order Function =  a function that either:
#                           1. accepts a function as an argument
#                               or
#                           2. returns a function
#                           (In python, functions are also treated as objects)

# ----- 1. accepts a function as an argument -----
def loud(text):
   return text.upper()

def quiet(text):
   return text.lower()

def hello(func):
   text = func("Hello")
   print(text)


hello(loud)
hello(quiet)
# ------------ 2. returns a function -------------
#def divisor(x):
   #def dividend(y):
       #return y / x
   #return dividend


#divide = divisor(2)
#print(divide(10))

print("""****************************************************************************
**************************  51 AULA: Python lambda λ ***********************
****************************************************************************""")
# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
# lambda parameters:expression

double = lambda x: x * 2
print(double(1))

multiply = lambda x, y: x * y
print(multiply(1,2))

add = lambda x, y, z: x + y + z
print(add(1,2,3))

full_name = lambda first_name, last_name: first_name+" "+last_name
print(full_name("Bro","Code"))

age_check = lambda age: True if age >= 18 else False
print(age_check(18))

print("""****************************************************************************
**************************  52 AULA: Python sort ***************************
****************************************************************************""")
# sort() method   = used with lists
# sort() function = used with iterables

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))

grade = lambda grades:grades[1]
# students.sort(key=age)                                       # sorts current list
sorted_students = sorted(students,key=grade) # sorts and creates a new list

for i in sorted_students:
    print(i)
    
print("""****************************************************************************
**************************  53 AULA: Python map  ***************************
****************************************************************************""")
# map() =   applies a function to each item in an iterable (list, tuple, etc.)
#
# map(function,iterable)

store = [("shirt",20.00),
         ("pants",25.00),
         ("jacket",50.00),
         ("socks",10.00)]

to_euros = lambda data: (data[0],data[1]*0.82)
# to_dollars = lambda data: (data[0],data[1]/0.82)

store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)
    
print("""****************************************************************************
**************************  54 AULA: Python filter *************************
****************************************************************************""")
# filter() =    creates a collection of elements from an iterable,
#               for which a function returns true
#
#               filter(function, iterable)

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

age = lambda data:data[1] >= 18

drinking_buddies = list(filter(age, friends))

for i in drinking_buddies:
    print(i)
    
print("""****************************************************************************
**************************  55 AULA: Python reduce *************************
****************************************************************************""")
# reduce() = apply a function to an iterable and reduce it to a single cumulative value.
#            performs function on first two elements and repeats process until 1 value remains
#
# reduce(function, iterable)

import functools

letters = ["H","E","L","L","O"]
word = functools.reduce(lambda x, y,:x + y,letters)
print(word)

# factorial = [5,4,3,2,1]
# result = functools.reduce(lambda x, y,:x * y,factorial)
# print(result)

print("""****************************************************************************
**************************  56 AULA: Python list comprehension *************
****************************************************************************""")
# list comprehension =  a way to create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]
# --------------------------------------------------------------
squares = []                # create an empty list
for i in range(1,11):       # create a for loop
    squares.append(i * i)    # define what each loop iteration should do
print(squares)

# create a list AND defines what each loop iteration should do
squares = [i * i for i in range(1,11)]
print(squares)

# --------------------------------------------------------------
students = [100,90,80,70,60,50,40,30,0]

passed_students = list(filter(lambda x: x >= 60, students))
passed_students = [i for i in students if i >= 60]
# passed_students = [i if i >= 60 else "FAILED" for i in students]

print(passed_students)

# --------------------------------------------------------------
print("""****************************************************************************
**************************  57 AULA: Python dictionary comprehension *******
****************************************************************************""")
# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions
#
# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable}
# dictionary = {key: function(value) for (key,value) in iterable}
# -------------------------------------------------------------------------
cities_in_F = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

# -------------------------------------------------------------------------
# weather = {'New York': "snowing", 'Boston': "sunny", 'Los Angeles': "sunny", 'Chicago': "cloudy"}
# sunny_weather = {key: value for (key,value) in weather.items() if value == "sunny"}
# print(sunny_weather)

# -------------------------------------------------------------------------
# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
# print(desc_cities)

# -------------------------------------------------------------------------
# def check_temp(value):
    # if value >= 70:
        # return "HOT"
    # elif 69 >= value >= 40:
        # return "WARM"
    # else:
        # return "COLD"


# cities = {'New York': 32, 'Boston': 75, 'Los Angeles': 100, 'Chicago': 50}
# desc_cities = {key: check_temp(value) for (key,value) in cities.items()}
# print(desc_cities)

# -------------------------------------------------------------------------

print("""****************************************************************************
**************************  58 AULA: Python zip function *******************
****************************************************************************""")
# zip(*iterables) =  aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_dates = ["1/1/2021","1/2/2021","1/3/2021"]

# --------------------------------------
users = list(zip(usernames,passwords))

for i in users:
    print(i)

# --------------------------------------
users = dict(zip(usernames,passwords))

for key,value in users.items():
    print(key+" : "+value)

# --------------------------------------
users = zip(usernames,passwords,login_dates)

for i in users:
    print(i)

# --------------------------------------
print("""****************************************************************************
**************************  59 AULA: Python if __name__ == '__main__'  *****
****************************************************************************""")
# ***********************************
# if __name__ == '__main__'
# ***********************************

# y tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the __name__ variable a value of '__main__' if it's
#  the initial module being run

def main():
    print("Hello!")


if __name__ == '__main__':
    main()
    
print("""****************************************************************************
**************************  60 AULA: Python time module  *******************
****************************************************************************""")
# *************************************************************************
import time
# *************************************************************************
print(time.ctime(0))    # convert a time expressed in seconds since epoch to a readable string
#                                        epoch = when your computer thinks time began (reference point)
print(time.time())      # return current seconds since epoch
print(time.ctime(time.time())) # will get current time

# *************************************************************************
# time.strftime(format, time_object) = formats a time_object to a string
# time_object = time.localtime() # local time
# time_object = time.gmtime()  # UTC time
# local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# print(local_time)

# *************************************************************************
# time.strptime(string_string, format) = parses a string representing time/date and returns a struct_time object
# time_string = "20 April, 2020"
# time_object = time.strptime(time_string,"%d %B, %Y")
# print(time_object)

# *************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and returns a string
# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.asctime(time_tuple)
# print(time_string)

# *************************************************************************
# time.asctime(time_tuple) = accepts a time_object or a tuple up to 9 elements and return seconds since epoch
# (year, month, day, hours, minutes, secs, day of the week, day of the year, dst)
# time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# time_string = time.mktime(time_tuple)
# print(time_string)

# *************************************************************************
print("""****************************************************************************
**************************  61 AULA: Python multithreading *****************
****************************************************************************""")
# ****************************************************
# Python threading tutorial
# ****************************************************
# thread =  a flow of execution. Like a separate order of instructions.
#                  However each thread takes a turn running to achieve concurrency
#                  GIL = (global interpreter lock),
#                  allows only one thread to hold the control of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time


def eat_breakfast():
    time.sleep(3)
    print("You eat breakfast")


def drink_coffee():
    time.sleep(4)
    print("You drank coffee")


def study():
    time.sleep(5)
    print("You finish studying")


x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

# ****************************************************
print("""****************************************************************************
**************************  62 AULA: Python daemon threads *****************
****************************************************************************""")
# **********************************************************
# Python daemon threads
# **********************************************************

# daemon thread = a thread that runs in the background, not important for program to run
#                 your program will not wait for daemon threads to complete before exiting
#                 non-daemon threads cannot normally be killed, stay alive until task is complete
#
#                 ex. background tasks, garbage collection, waiting for input, long running processes

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("logged in for: ", count, "seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

# x.setDaemon(True)
# print(x.isDaemon())

answer = input("Do you wish to exit?")

# **********************************************************
print("""****************************************************************************
**************************  63 AULA: Python multiprocessin *****************
****************************************************************************""")
# *********************************
# Python multiprocessing
# *********************************
# multiprocessing = running tasks in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count
import time


def counter(num):
    count = 0
    while count < num:
        count += 1


def main():

    print("cpu count:", cpu_count())

    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))

    a.start()
    b.start()

    print("processing...")

    a.join()
    b.join()

    print("Done!")
    print("finished in:", time.perf_counter(), "seconds")


if _name_ == '__main__':
    main()

# *********************************
print("""****************************************************************************
**************************  64 AULA: Python GUI windows  *******************
****************************************************************************""")
#https://www.youtube.com/watch?v=lyoyTlltFVU&list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT&index=66
from tkinter import *

window = Tk() #instantiate an instance of a window
window.geometry("420x420")
window.title("Bro Code first GUI program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop() #place window on computer screen, listen for events

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
**************************  97 AULA: Python calculator program *************
****************************************************************************""")
# **************************************************************
# Python Calculator
# **************************************************************
from tkinter import *

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text

    try:

        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:

        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:

        equation_label.set("arithmetic error")

        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()
window.title("Calculator program")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3, column=0)

plus = Button(frame, text='+', height=4, width=9, font=35,
                 command=lambda: button_press('+'))
plus.grid(row=0, column=3)

minus = Button(frame, text='-', height=4, width=9, font=35,
                 command=lambda: button_press('-'))
minus.grid(row=1, column=3)

multiply = Button(frame, text='*', height=4, width=9, font=35,
                 command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text='/', height=4, width=9, font=35,
                 command=lambda: button_press('/'))
divide.grid(row=3, column=3)

equal = Button(frame, text='=', height=4, width=9, font=35,
                 command=equals)
equal.grid(row=3, column=2)

decimal = Button(frame, text='.', height=4, width=9, font=35,
                 command=lambda: button_press('.'))
decimal.grid(row=3, column=1)

clear = Button(window, text='clear', height=4, width=12, font=35,
                 command=clear)
clear.pack()

window.mainloop()

print("""****************************************************************************
**************************  98 AULA: Python text editor program ************
****************************************************************************""")
# ************************************
# Python Text Editor
# ************************************
import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="pick a color...or else")
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    window.title("Untitled")
    text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")

            text_area.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()


def save_file():
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't save file")

        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo("About this program", "This is a program written by YOUUUUU!!!")


def quit():
    window.destroy()


window = Tk()
window.title("Text editor program")
file = None

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

font_name = StringVar(window)
font_name.set("Arial")

font_size = StringVar(window)
font_size.set("25")

text_area = Text(window, font=(font_name.get(), font_size.get()))

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)

frame = Frame(window)
frame.grid()

color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

window.mainloop()

print("""****************************************************************************
**************************  99 AULA: Python Tic Tac Toe game ***************
****************************************************************************""")
# ******************************************************
# Python Tic Tac Toe game
# ******************************************************

from tkinter import *
import random

def next_turn(row, column):

    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():

    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")


window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row,column=column)

window.mainloop()

# ******************************************************

print("""****************************************************************************
**************************  100 AULA: Python snake game  ********************
****************************************************************************""")
# ************************************
# Python Snake
# ************************************
from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)


class Food:

    def __init__(self):

        x = random.randint(0, (GAME_WIDTH / SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()

    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_collisions(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)


def change_direction(new_direction):

    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction


def check_collisions(snake):

    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False


def game_over():

    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2,
                       font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")


window = Tk()
window.title("Snake game")
window.resizable(False, False)

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn(snake, food)

window.mainloop()
