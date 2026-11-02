#data type conversation
#1 . int() function is used to convert a string or float into an integer.
#2 . float() function is used to convert a string or integer into a float.
#3 . str() function is used to convert an integer or float into a string.
#4 . bool() function is used to convert a string, integer or float into a boolean value.

# a = 12
# a = str(a)
# print(type(a)) 

# b = 12.5
# b = int(b)
# print(type(b)) 

# c = "True"
# c = bool(c)
# print(type(c)) 
# print(c) 

# d = 12.5
# d = str(d)
# print(type(d)) 

# e = True
# e = int(e)
# print(type(e))
# print(e)

# f = "12.12"
# f = int(f)
# print(type(f))
# print(f)
#we can not change a string with decimal point into an integer directly, it will give an error we need to convert 
# it to a float first and then to an integer.

#there are some values which give boolean value as false when converted to boolean value. They are:
#1 . 0
#2 . 0.0
#3 . "" (empty string)
#4 . [] (empty list)
#5 . {} (empty dictionary)
#6 . () (empty tuple)
#7 . False, None
# else all are true when converted to boolean value.

#input and output
# for output we all know we use print() function to print the output on the screen.
# we are using input() function to take input from the user. 
# Whatever the user enters is considered as a string. if we want to take input as an integer or float
# we need to convert it into integer or float using int() or float() function.

# name = "Divyadeep"
# age = 25
# #1st this is first way.

# print("hello how are you", name, "your age is", age)

# #2nd in this way we use f string to print thr output. f string is used to format the string. we can use variables
# #inside the string using {}. we can call it functional string.

# print(f"hello how are you {name} your age is {age}")

# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# print("your name is :", name)
# print("your age is :",age)
# print(f"hello how are you {name} your age is {age}")

