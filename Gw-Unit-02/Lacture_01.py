# Odd/Even

# x=int(input("Enter the any number: "))
# if x%2==0:
#     print("Even")
# else:
#     print("Odd")


# largest number

# x=int(input("Enter the 1st number: "))
# y=int(input("Enter the 2nd number: "))
# z=int(input("Enter the 3rd number: "))
# if x>y and x>z:
#     print(f"{x} is a largest number ")
# elif y>x and y>z:
#     print(f"{y} is a largest number ")
# else:
#     print(f"{z} is a largest number ")



# x=int(input("Enter the 1st number: "))
# y=int(input("Enter the 2nd number: "))
# z=int(input("Enter the 3rd number: "))
# if x>y:
#     if x>z:
#         print(f"{x} is a largest number ")
#     else:
#         print(f"{z} is a largest number ")
# else:
#     if y>z:
#         print(f"{y} is a largest number ")
#     else:
#         print(f"{z} is a largest number ")




# calculator

# x=int(input("Enter the 1st number: "))
# y=int(input("Enter the 2nd number: "))
# z=(input("Enter any one operator +,-,*,/,//,%: "))
# if z=='+':
#     print("sum = ",x+y)
# elif z=='-':
#     print("sub = ",x-y)
# elif z=="*":
#     print("mul = ",x*y)
# elif z=="/":
#     print("div = ",x/y)
# elif z=="//":
#     print("floor div = ",x//y)
# else:
#     print("modlus = ",x%y)




# leap year or not

# x=int(input("Enter the year: "))
# if x%400==0:
#     print(f"{x} is a leap year.")
# elif x%100==0:
#     print(f"{x} is not a leap year.")
# elif x%4==0:
#     print(f"{x} is a leap year.")
# else:
#     print(f"{x} is not a leap year.")



# root of quadric equation

# from math import sqrt
# a=float(input("Enter the value a: "))
# b=float(input("Enter the value b: "))
# c=float(input("Enter the value c: "))
# d = b*b-4*a*c
# if d>0:
#     print("Roots are real and different:")
#     r1=(-b+sqrt(d))/(2*a)
#     r2=(-b-sqrt(d))/(2*a)
#     print("Root_1 = ",r1)
#     print("Root_2 = ",r2)
# elif d==0:
#     print("Roots are real and same:")
#     r1=r2=-b/(2*a)
#     print("Root_1 = ",r1)
#     print("Root_2 = ",r2)
# else:
#     print("Roots are imaginary")



# print revers order

# fname = input("Enter the first name: ")
# lname = input("Enter the last name: ")
# print("Hello "+lname+" "+fname)



'''Write a Python program that accepts a
 sequence of comma-separated numbers from
 the user and generates a list and a tuple of
 those numbers.'''

# values=input("Enter the comma separeted value: ")
# list1=values.split(",")
# print(list1)
# tup1=tuple(list1)
# print(tup1)



'''Write a Python program to display the first and
 last colors and middle element from the list'''

# color=["Red","Green","Blue","Yellow","Purple"]
# print("First color: ",color[0])
# print("Last color: ",color[-1])
# print("Middle color: ",color[5//2])




'''Write a Python program that accepts an integer (n) and computes the value of
 n+nn+nnn.
 '''

# n=int(input("Enter the number: "))
# n1=n
# n2=n*n
# n3=n*n*n
# print(n1+n2+n3)


''' Write a Python program to count the number 4 in a
 given list.'''

# number=[1,4,3,4,5,6,4,8,9]
# y=number.count(4)
# print("The number of 4s in the list: ",y)


''' Write a Python program to calculate the number of days 
between two dates. Sample dates : (2014, 7, 2), (2014, 7, 11)'''

# from datetime import date
# first_date=date(2014,7,2)
# last_date=date(2014,7,12)
# z=last_date-first_date
# print(z.days)


'''Python program that takes a
 string and a non-negative integer
 n, then returns n copies of the
 first two characters of the given
 string'''

# str1="Python"
# n=3
# x=str1[0:2]
# result=x*n
# print(result)


''' Write a Python program to test whether a passed letter is a
 vowel or not'''

# letter=input("Enter a letter: ")
# if letter in 'aeiouAEIOU':
#     print(letter,"is vowel.")
# else:
#     print(letter,"is consonant.")


''' Write a Python program that concatenates all elements
 in a list into a string and returns it.'''

# elements=["Hello","World","This"]
# result=''.join(elements)
# print(type(result))
# print("concatenated string",result)



'''Write a Python program to sum three given integers.
 However, if two values are equal, the sum will be
 zero'''

# num1=int(input("Enter the first numer: "))
# num2=int(input("Enter the second numer: "))
# num3=int(input("Enter the third numer: "))
# if num1 == num2 or num2 ==num3 or num3==num1:
#     result = 0
#     print("The result is = ",result)

# else:
#     result = num1+num2+num3
#     print("The result is = ",result)


''' Write a Python program to sum two
 given integers. However, if the sum is
 between 15 and 20 it will return 20'''

# num1=int(input("Enter the first numer: "))
# num2=int(input("Enter the second numer: "))
# result = num1+num2
# if 15<=result<=20:
#     result= 20
# print("The result is",result)



'''Write a Python program to add two objects if both
 objects are integers.'''

# obj1=input("Enter the first object: ")
# obj2=input("Enter the second object: ")
# if obj1.isdigit() and obj2.isdigit():
#     result=int(obj1)+int(obj2)
#     print("The sum is :",result)
# else:
#     print("Both object are not object.")


'''Write a Python program to parse a string to float or integer'''

# n="246.2458"
# print(float(n))
# print(int(float(n)))


'''Calculate the hypotenuse of a right angled triangle'''

# from math import sqrt
# print("Input lengths of shorter triangle side: ")
# a = float(input("a = "))
# b = float(input("b = "))
# c= sqrt(a**2+b**2)
# print("The length of hypotenuse is: ",c)


''' Write a Python program to count the number of occurrences of a specific character in a string.'''

# s=input("Enter the string: ")
# c=input("Enter the character to count: ")
# z=s.count(c)
# print(z)



'''Write a Python program to remove the
 first item from a specified list'''

# my_list=['apple','banana','cherry','date']
# if my_list:
#     my_list.pop(0)
# print("Updated list: ",my_list)


'''Write a Python program to test whether all
 numbers in a list are greater than a certain number.'''

# number=[10,20,30,40,50]
# threshold=int(input("Enter the thershold number: "))
# if all(num>threshold for num in number):
#     print("Yes")
# else:
#     print("false")


'''Write a Python program to sum all the  items in a list'''

# number=[1,2,3,4,5]
# result=0
# for num in number:
#     result +=num
# print("The sum of all item is:",result)


''' Write a Python program to multiply all the items in a list'''

# number=[1,2,3,4,5]
# result=1
# for num in number:
#     result *=num
# print("The product of all item is:",result)


''' Write a Python program to get the largest number
 from a list'''

# number=[10,25,47,3,99,56]
# largest=number[0]
# for num in number:
#     if num>largest:
#         largest=num
# print("The largest number is : ",largest)


''' Write a Python program to get the smallest number
 from a list'''

# number=[10,25,47,3,99,56]
# smallest=number[0]
# for num in number:
#     if num<smallest:
#         smallest=num
# print("The smallest number is : ",smallest)


'''Write a Python program to count the number of strings from a given list of
 strings. The string length is 2 or more
 and the first and last characters are the
 same'''

# strings=['abc','xyz','aba','1221','a']
# count=0
# for s in strings:
#     if len(s)>=2 and s[0]==s[-1]:
#         count +=1
# print(count)