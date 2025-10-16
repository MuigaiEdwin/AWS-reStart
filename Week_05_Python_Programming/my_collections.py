#lists

myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#Accessing a list by position
print(myFruitList[0])   # this is accessing the banana

print(myFruitList[1]) # this is accessing banana

print(myFruitList[2]) #this is accessing the  cherry


#Changing the values in a list

myFruitList[2]= "orange"
print(myFruitList)   #THIS IS NOW THE UPDATED LIST WITH ORANGE



#Exercise 2: Introducing the tuple data type

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))


#Accessing a tuple by position

print(myFinalAnswerTuple[0])  #>> accessing the apple

print(myFinalAnswerTuple[1])

print(myFinalAnswerTuple[2])


#Exercise 3: Introducing the dictionary data type
myFavouriteFruitDictionary = {
    "Akua" : "apple",
    "Saanvi" : "banana",
    "Paulo" : "pineapple"
}

print(myFavouriteFruitDictionary)

#Accessing a dictionary by name
print(myFavouriteFruitDictionary["Akua"]) #

print(myFavouriteFruitDictionary["Saanvi"])

print(myFavouriteFruitDictionary["Paulo"])


