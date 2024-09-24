#Print i as long as i is less than 6:
i = 1
while i < 6:
  print(i)
  i += 1
  
  #Exit the loop when i is 3:
  i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1
  
  # Note that number 3 is missing in the result
  i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  #Loop through the letters in the word "banana":
  
  for x in "banana":
  print(x)
  
  #Exit the loop when x is "banana":
  fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Using the range() function: ptint from 0 to 5
for x in range(6):
  print(x)
  
  #Increment the sequence with 3 (default is 1):
  for x in range(2, 30, 3):
  print(x) 
  
  
  #Print each adjective for every fruit:
  adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
    
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


#Dictionaries cannot have two items with the same key:   
#Duplicate values will overwrite existing values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

#Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


#Get the value of the "model" key:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)


#Change the "year" to 2018:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)

#Update the "year" of the car by using the update() method
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

print(thisdict)

#Adding an item to the dictionary is done by using a new index key and assigning a value to it
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#Make a copy of a dictionary with the dict() function:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

#Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

#The popitem() method removes the last inserted item 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

#The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

#Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
