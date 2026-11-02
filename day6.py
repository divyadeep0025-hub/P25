#conditional statements 

#let's take a example of age of voting

# age = int(input("write your age : "))

# if age >= 18:
#     print("Congratulations you are eligible for voting.")

# else :
#     print(f"Sorry you are not eligible for voting now, try after {18 - age} years.")

#using if elif else

# money = int(input("How much money you have : "))

# if money == 10:
#     print("you will have chochlate")

# elif money == 20:
#     print("you will have soft drink")

# elif money == 50:
#     print("you will have burger")

# elif money == 100:
#     print("you will have 2 burger.")

# elif money == 200:
#     print("you will have paneer kulche")

# else :
#     print("you will have proper 2 person meal")

#lets have some fun

#1 accept two numbers and print greater one

# a = int(input("number 1 : "))
# b = int(input("number 2 : "))

# if a > b :
#     print(f"{a} is greater than {b} ")

# elif b > a :
#     print(f"{b} is greater than {a}")

# else :
#     print("both numbers are equal")

# accept an integer and check whether it is an even number or odd number

a = int(input("enter a number : "))

if a % 2 == 0:
    print(f"{a} is an even number")

else :
    print(f"{a} is an odd number")