# Q1. Print Numbers from 1 to N
# Take an integer N as input from the user and print all the numbers from 1 to N using a for loop.
# Example:  1 2 3 4 5 

# n = int(input("enter a number : "))

# for i in range(1,n+1,1):
#     print(i)


# Q2. Print Even Numbers
# Take an integer N as input and print all the even numbers from 1 to N using a for loop.
# Example :  let n = 10 ,  output : 2 4  6 8 10

# n = int(input("enter a number : "))

# for i in range(1,n+1):
#     if i % 2 == 0:
#         print(i)

# Q3. Print Odd Numbers
# Take an integer N as input and print all the odd numbers from 1 to N using a for loop.
# Example :  let n = 10 ,  output : 1 3 5 7 9

# n = int(input("enter a number : "))

# for i in range(1,n+1):
#     if i % 2 != 0:
#         print(i)

# Q4. Find the Sum from 1 to N
# Take an integer N as input and calculate the sum of all numbers from 1 to N using a for loop.
# Example :  let n = 5 ,  sum : 15

#N = int(input("enter a number : "))

n = 5 
sum = 0 
for i in range(1,n+1):
    sum = sum + i
print(sum)
    
























# Q5. Multiplication Table
# Take an integer N as input and print its multiplication table from 1 to 10 using a for loop.
# Example :  N=7 , 7 * 1 =7 like this till 7*10=70
# n = int(input("enter a number : "))
# for i in range(n,n*10+1,n):
#         print(i)

# Q6. Print Each Character
# Take a string as input from the user and use a for loop to print each character on a separate line.
# Example :   let S=”python”,  
# output :
#  p
# y 
# t
# h 
# o 
# n

n = input("enter a string : ")

for i in n[::-1]:
    print(i)


# Q7. Print the Table of -6
# Write a program to print the multiplication table of -6
# Example :  let n = -6, 
#  output : 
# -6
# -12
# -18
# till ….. -60

# n = int(input("enter a number : "))

# for i in range(n,n*10-1,n):
#         print(i)

# a second way of write...... if and else condition statement

# age = 21
# print("can vote" if age > 18 else "cannot vote")