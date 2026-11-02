#take inputs of principal , rate and time from user and calculate simple interest
#the simple interest formula is SI = (P * R * T) / 100

# P = int(input("Enter the principal amount: "))
# R = float(input("Enter the rate of interest: "))
# T = int(input("Enter the time in years: "))

# #SI = (P * R * T) / 100

# #print(f"The simple interest is: {SI}")

# #compound interest formula is CI = P * (1 + R/100) ** T

# CI = (P * (1 + (R/100)) ** T) - P
# print(f"The compound interest is: {CI}")

# print((12 == 45 or 23 == 45 or not 12 != 12) and (bool(34) and 34 == 34))

#1 
a = 15
b = 10
c = 20

print(f"answer of question 1 is : {a > b and c > a}") #TRUE

#2
x = 25
y = 30

print(f"answer of question 2 is : {x < 20 or y >= 30}") #TRUE

#3
a = 10
b = 20
c = 10

print(f"answer of question 3 is : {a == c and b != c}") #TRUE

#4
x = 15

print(f"answer of question 4 is : {x >= 10 and x <= 20 and x != 15}") #FALSE

#5 
a = 5
b = 1
c = 15

print(f"answer of question 5 is : {(a < b or b > c) and c != 15}") #FALSE

#6
x = 15

print(f"answer of question 6 is : {not(x > 10 and x < 20)}") #FALSE

#7
a = 5
b = 1 
c = 15

print(f"answer of question 7 is : {(a < b or b > c) and c != a}") #FALSE

#8
a = 10
b = 20
c = 30

print(f"answer of question 8 is : {(a == b or b < c) and c != a}") #TRUE

#9
a = 10
b = 20
c = 10

print(f"answer of question 9 is : {(a == c or b > a) or (a > b and c != 10)}") #TRUE

#10
a = 10
b = 20
c = 10

print(f"answer of question 10 is : {(a < b and b < c) or not(c < a or a == c)}") #FALSE