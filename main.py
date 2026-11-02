# print('hello youtube we are learning python through you')
# #we are going to use function string using F keywords and also use curly brackets for using variable in string
# name = "Divyadeep"
# age = 26

# print(f"My name is {name} and my age is {age}")

# input("my name is :")

# ord function is used for knowing the unicode value of string
# print(ord("a"))
# print(ord("b"))

# print(True and bool(0))

# conditional statment

# money = int(input("Please provide me money :- "))

# if money == 10:
#     print("I will have a choco Bar icecream")

# elif money == 20:
#     print("I will have a mango dolly")
# else:
#     print("I will have a cone icecream")

# num1 = int(input("write number 1 :-"))

# num2 = int(input("write number 1 :-"))

# if num1 > num2:
#     print(f"{num1} is greater then {num2}")

# elif num2>num1 :
#         print(f"{num2} is greater then {num1}")

# else:
#       print("both number are same")  

# gen = input("Please tell me your gender as a alphabet(M or F or m or f):-")

# if gen == "M" or gen == "m":
#     print("Good morning SIR")

# elif gen == "F" or gen == "f":
#     print("Good morning MAM")

# else :
#     print("Unidentified Gender")

# num = int(input("Please write your number:-"))

# if num%2 == 0 :
#     print(f"{num} is even")

# else :
#     print(f"{num} is odd")
 

# name = input("please tell me your name:-")

# age = int(input("please tell me your age:-"))

# if age >= 18 :
#     print(f"hello {name} you are a valid voter")

# else :
#     print(f"Hello {name} you are not a valid voter and you are able to voter after {18-age} years thank you for applying.")

# year = int(input("enter year :- "))

# if year % 100 == 0 and year % 400 == 0:
#     print(f"{year} is a leap year")

# elif year % 100 != 0 and year % 4 ==0 :
#     print (f"{year} is a leap year")

# else:
#     print(f"{year} is a normal year")

# t = float(input("enter the temprature :- "))

# if t < 0 :
#     print(f"{t} is freezing cold")

# elif t>=0 and t<10:
#     print(f"{t} is very cold")

# elif t>=10 and t<20:
#     print(f"{t} is cold")

# elif t>=20 and t<30:
#     print(f"{t} is pleasant")

# elif t>=30 and t<40:
#     print(f"{t} is hot")

# else:
#     print(f"{t} is very hot")

# a = range(1,20,1)

# n = int(input("write down no for your table:-"))

# for i in range(n,n*10+1,n):
#     print(i)

# a = "SHERIYANS HELP STUDENTS IN THEIR CARRIER"

# for i in range(len(a)):
#     print(a[i])

# a = "DIVYADEEP IS A GOOD PERSON"

# for i in a:
#     print(i)

#accept an integer and print hello world n times

# n = int(input("enter a number :- "))

# for i in range(n):
#     print("Hello world")

#print natural number up to n

# n = int(input("enter a number :- "))

# for i in range(1,n+1):
#     print(i)

#reverse for loop. Print n to 1
# n = int(input("enter a number :- "))

# for i in range(n,0,-1):
#     print(i)

#take a number and print the table of that number
# n = int(input("which number table you want :- "))

# for i in range(1,11):
#     print(f"{n}*{i} = {n*i}")

#sum up to n number 

# n = int(input("enter a number :- "))

# sum = 0

# for i in range(1,n+1):
#     sum = sum + i

# print(f"your sum is {sum}")

#factorial of a number

# n = int(input("enter a number :- "))

# fact = 1 

# for i in range(1,n+1):
#     fact = fact * i

# print(f"your factorial is {fact}")

#print the sum of all even numbers and odd numbers in a range seprately

# n = int(input("enter a number :- "))

# even_sum = 0
# odd_sum = 0 

# for i in range(n):
#     if i%2 == 0:
#         even_sum = even_sum + i
#     else:
#         odd_sum = odd_sum + i  

# print(f"your even number sum is {even_sum} and your odd number sum is {odd_sum}") 

# find the factor of a given number

# n = int(input("enter a number :- "))

# for i in range(1,n+1):
#     if n%i == 0:
#         print(f"{i} is a factor of {n}")  

# accept a number and check if it is a perfect number or not.

# n = int(input("enter a number :- "))

# sum = 0

# for i in range(1,n):
#     if n%i == 0:
#         print(f"{i} is a factor of {n}")

# if sum == n:
#     print(f"{n} is a perfect number")

# else :
#     print(f"{n} is not a perfect number")

# check the given number is a prime number or not'

# n = int(input("enter a number :- "))

# count = 0

# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1

# print(count)

# if count == 2:
#     print(f"{n} is a prime number")

# else:
#     print(f"{n} is not a prime number")

# using for loop reverse the string

# a = "DIVYADEEP IS A GOOD PERSON"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# print(b)

# check the string is palindrome or not using for loop

# a = input("enter a string :- ")
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if a == b:
#     print("The string is a palindrome")
# else:
#     print("The string is not a palindrome")

#count the all letters digit and special character in a string

# a = "abdkhjd245415%$^%*&#^#"

# char = 0
# digit = 0
# special = 0

# for i in a:
#     if i.isalpha():
#         char = char + 1
#     elif i.isdigit():
#         digit = digit + 1
#     else:
#         special = special + 1

# print(f"Number of letters: {char}")
# print(f"Number of digits: {digit}")
# print(f"Number of special characters: {special}")

#some questions on while loop

# seperate each digit of a number and print it on the new line

# a = int(input("enter a number :- "))

# while a > 0:
#     print(a % 10)
#     a = a // 10

#accept a number and print it in reverse order and also print each digit on a new line

# a = int(input("enter a number :- "))

# rev = 0

# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(f"your reverse number is {rev}")

# while rev > 0:
#     print(rev % 10)
#     rev = rev // 10 

# accept a number and check if it is a palindrome or not using while loop

# a = int(input("enter a number :- "))

# rev = 0
# copy = a

# while a > 0:
#          rev = rev * 10 + a % 10
#          a = a // 10

# if copy == rev:
#     print(f"{copy} is a palindrome number")
# else:
#     print(f"{copy} is not a palindrome number")

#create a random number guessing game using while loop in python

# import random

# num = random.randint(1,100)
# tries = 0

# while True:
#     guess = int(input("Guess a number between 1 and 100: "))

#     if num == guess:
#         tries += 1
#         print(f"Congratulations! You guessed the correct number in {tries} tries.")
#         break

#     elif guess < num:
#         tries += 1
#         print("Your guess is too low. Try again.")

#     elif guess > num:
#         tries += 1
#         print("Your guess is too high. Try again.")
#     else:
#         tries += 1
#         print(f"Sorry, the correct number was {num}. Better luck next time!")

# we are going to learn about user define function in python.

# positional argument function

# def add(a,b):
#     print(f"your sum is {a+b}")

# add(10,20)

# keyword argument function

# def hello(name,age):
#     print(f"Hello {name} your age is {age}")

# hello(age = 26 , name = "Divyadeep")

#default argument function

# def sum(a,b=10):
#     print(f"your sum is {a+b}")

# sum(10)

# lets create a function which will find weather string is palindrome or not

# def is_palindrome(s):
#     rev = ""
#     for i in range(len(s)-1,-1,-1):
#         rev = rev + s[i]

#     if rev == s:
#         print(f"{s} is a palindrome string")
#     else:
#         print(f"{s} is not a palindrome string")

# is_palindrome(input("enter a string :- "))

# lets work on the list a part of data structure in python

#Q1 - print positive and negative number from a list

# l = [10, -20, 30, -40, 50, -60]

# print("Positive numbers in the list:")
# for i in l:
#     if i >= 0:
#         print(i)

# print("Negative numbers in the list:")
# for i in l:
#     if i < 0:
#         print(i)

#Q2 - find the mean of a list elements

# l = [10, 58, 49, 57, 55]

# sum = 0
# for i in l:
#     sum += i

# print(f"The mean of the list elements is: {sum/len(l)}")

#Q3 - find the largest element and its index from a list

# l = [45,54,455,454,2248,1455,200]

# largest = l[0]
# index = 0 

# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#         index = i

# print(f"The largest element in the list is: {largest} and its index is: {index}")

#Q4 - find the second greatest element from a list

# l = [45,54,455,454,200]

# largest = l[0]
# second_largest = l[0]

# for i in l:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest:
#         second_largest = i

# print(f"The second largest element in the list is: {second_largest} and the largest element is: {largest}")

#Q5 - find the list is sorted or not

# l = [1, 2, 3, 4, 5]

# for i in range(len(l)-1):
#     if l[i] < l[i + 1]:
#         continue

#     else:
#         print("The list is not sorted.")
#         break
# else:
#     print("The list is sorted.")


#lets have some info about tuple in python

# There are two types of method in tuple which we are going to see here

#first is index and second is count method

# a = (1,2,3,4,5,5,5,5,5,5,6,7)

# index = a.index(5)
# count = a.count(5)

# print(f"The index of 5 in the tuple is: {index}")
# print(f"The count of 5 in the tuple is: {count}")

# We can also unpack the tuple into variables but if we give one one variable then it will become int.
# a,b,c,d = (1,2,3,4)

# print(a)

# some method of sets in python

# s = {1,2,3,4,5,6,7,8,9}

# s.add(10)
# s.remove(5)
# s.pop()
# s.discard(3)
# s.clear()

# print(s)

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

#s = a.union(b)
        # s = a|b
#s = a.intersection(b)
        # s = a&b
#s = a.difference(b)
        # s = a-b
#s = a.symmetric_difference(b)
        # s = a^b
#print(s)

# some function of dictionary in python

# d = {10:100, 20:200, 30:300, 40:400}

# d[10] = 1000 #update the value of key 10
# d[50] = 5000 # add a new key-value pair to the dictionary
# del d[20] # delete the key-value pair with key 20
# print(d)

#traversing a dictionary using for loop 
# d = {10:100, 20:200, 30:300, 40:400}

# for i in d:
#     print(i, d[i])

# another way to traverse a dictionary using for loop

# d = {10:100, 20:200, 30:300, 40:400}

# for i in d:
#     print(i)


import webbrowser
webbrowser.open("https://www.youtube.com/watch?v=VchuKL44s6E&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=1")