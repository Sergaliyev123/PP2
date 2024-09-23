import sys
print("Hello, World!")


print(sys.version)

if 5 > 2:
  print("Five is greater than two!")

#The number of spaces is up to you as a programmer, the most common use is four, but it has to be at least one.
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 
        
        x=5
        y="Hello world"
        print(x)
        print (y)
#this is a comment


#Comments starts with a #, and Python will ignore them:
#A comment does not have to be text that explains the code, it can also be used to prevent Python from executing code
#print("Hello, World!")
print("Cheers, Mate!") #this is a comment

#Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)  #output sally

#If you want to specify the data type of a variable, this can be done with casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#You can get the data type of a variable with the type() function
x = 5
y = "John"
print(type(x))  #int
print(type(y))  #str(string)


#double quotes are the same as single quotes:
x = "John"
print(x)
x = 'John'
print(x)

#And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

#If you have a collection of values in a list. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x)
print(y)
print(z)

#output is print()
x = "Python "
y = "is "
z = "awesome "
print(x, y, z)
print(x+y+z)

#IT will be error srting + int
#x = 5
#y = "John"
#print(x + y)

#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# We create a variable inside a function, with the same name as the global variabl
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = 1
y = 2.8
z = 1j

print(type(x)) #<class 'int'>
print(type(y)) #<class 'float'> дробь
print(type(z)) #<class 'complex'>

#tipe of float
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


#convert from int to float:
x = float(1)
#convert from float to int:
y = int(2.8)
#convert from int to complex:
z = complex(1)
print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#Import the random module, and display a random number between 1 and 9:
import random

print(random.randrange(1, 10))

#чтобы написать бесь текст на раз строчках
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


b = "Hello, World!"
print(b[2:5]) #llo

#begin from end, but reversed
b = "Hello, World!"
print(b[-5:-2])  #orl

b = "Hello, World!"
print(b[:5]) #Hello

#The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())

#The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())

#The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#To specify a string as an f-string, simply put an f n front of the string literal, and add curly brackets {} as placeholders for variables and other operations. 
age = 36
txt = f"My name is John, I am {age}"
print(txt)


#You will get an error if you use double quotes inside a string that are surrounded by double quotes:
txt = "We are the so-called "Vikings" from the north."

#The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)



#Boolean Values  output will be true or false
print(10 > 9)
print(10 == 9)
print(10 < 9)

#The following will return True
print(bool("Hello"))
print(bool(15))

#The following will return False:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#You can create functions that returns a Boolean Value:
def myFunction() :
  return True

print(myFunction())


#Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
  
  #This will return the items from position 2 to 5.
  thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

#Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

#Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist) 

#Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
  #Without list comprehension you will have to write a 'for' statement with a conditional test inside
  fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#analog
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

#Sort the list descending
thislist = [100, 50, 65, 82, 23]

thislist.sort(reverse = True)

print(thislist)


#Make a copy of a list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()  #mylist = list(thislist) list()
print(mylist)

#Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
  #set
  #Sets cannot have two items with the same value.
  thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#To determine how many items a set has. len()
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Check if "banana" is present in the set
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

#Check if "banana" is NOT present in the set:
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#The union() and update() methods joins all items from both sets.
#The intersection() method keeps ONLY the duplicates.

#The difference() method keeps the items from the first set that are not in the other set(s).

#The symmetric_difference() method keeps all items EXCEPT the duplicates.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#Join a set with a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b

#The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
  #One line if else statement, with 3 conditions:
  a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#The and,or,NOT keyword is a logical operator, and is used to combine conditional statements
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
  #You can have if statements inside if statements, this is called nested if statements
  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
    
    
  