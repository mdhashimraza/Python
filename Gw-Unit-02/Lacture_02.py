# range()    range(start,end)    range(start,end,step) 

# for i in range(6):
#     print(i,end=" ")
# print()

# for i in range(1,6):
#     print(i,end=" ")
# print()


# for i in range(1,20,4):
#     print(i,end=" ")
# print()


'''Write a for loop that prints number from 0 to 57
 using range function'''

# for i in range(58):
#     print(i,end=" ")


'''write a program to check whether a 
number is Armstrong or not'''

# n=int(input("Enter the number: "))
# sum=0
# num=n
# while n>0:
#     digit=n%10
#     sum += digit**3
#     n//=10
# if num==sum:
#     print("Armstrong")
# else:
#     print("Not Armstrong")


'''write a program to find out the whether a number
 is palindrome or not'''

# n=int(input("Enter the any number: "))
# num=n
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print("Revers = ",rev)
# if num==rev:
#     print("Plindrome")
# else:
#     print("Not Plindrome")


'''write a  program to find out the fibonnaci
 series upto n term'''


# nterm=int(input("How many terms? "))
# n1,n2=0,1
# count=0
# if nterm<=0:
#     print("Please enter a positive number:")
# elif nterm==1:
#     print(n1)
# else:
#     print("Fabonacci sequence")
#     print(n1,n2,end=" ")
#     for i in range(3,nterm+1):
#         nth=n1+n2
#         print(nth,end=" ")
#         n1=n2
#         n2 = nth


'''Write a program to find out the factorial of a
 number'''

# num=int(input("Enter the any number: "))
# fac=1
# if num<0:
#     print("Sorry, Factorial does not exit for negative number:")
# elif num==0:
#     print(f"The factorial of {num} is 1")
# else:
#     for i in range(1,num+1):
#         fac=fac*i
#     print(f"The factorial of {num} is",fac)


'''write a program to check whether a number 
is prime  or not'''

# num=int(input("Enter a number: "))
# flag=False
# if num==1:
#     print(num,"is not a prime number")
# elif num>1:
#     for i in range(2,num):
#         if num%i==0:
#             flag=True
#             break
#     if flag:
#         print(num,"is not a prime number")
#     else:
#         print(num,"is a prime number")
# else:
#     print("enter the positive number")


'''write a program to print the reverse of a number'''

# n=int(input("Enter the any number: "))
# rev=0
# while n>0:
#     digit=n%10
#     rev=rev*10+digit
#     n//=10
# print("Revers number =",rev)


''' What will be the output?'''

# i=0
# while i<3:
#     print(i)
#     i+=1
# else:
#     print(0)


'''write a program to convert time from 12 hour to 24 hour format'''

# str1="12:05:45"
# if str1[-2:]=="AM" and str1[:2]=="12":
#     print("00"+str1[-2:2])
# elif str1[-2:]=="AM":
#     print(str1[:-2])
# elif str1[-2:]=="PM" and str1[:2]=="12":
#     print(str1[:-2])
# else:
#     print(str(int(str1[:2])+12)+str1[2:8])


# Break and Continue statement

# print("Break statement")
# for i in range(10):
#     if i ==5:
#         break
#     print(i)


# print("Continue statement")
# for i in range(10):
#     if i ==5:
#         continue
#     print(i)



# pass

# li=['a','b','c','d']
# for i in li:
#     if i=='a':
#         pass
#     else:
#         print(i)


'''Write a program to print the prime number in range'''

lower=int(input("Enter the lower range:"))
upper=int(input("Enter the upper range:"))
print(f"Prime number between {lower} and {upper} are: ")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)