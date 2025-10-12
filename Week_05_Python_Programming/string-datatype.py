myString = "This is a string."
print(myString)

#to get the data type of the variable.
print(type(myString))

print(myString + " is of datatype " + str(type(myString)))


#Concatenation - adding  to sentences or words into one  using the +

firstString = "Water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)


# Getting the information from the user  using the input 

name = input("What is your name??")
print(name)


#Formatting output strings
color = input("What is your favourite color??")
animal = input("What is your favourite animal??")

print("{}, you like a {} {}!".format(name,color,animal))