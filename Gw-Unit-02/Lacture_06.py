'''1. Write a Python program to replace the last element in a list with another list. Sample data : [1, 3, 
5, 7, 9, 10], [2, 4, 6, 8]  Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]'''

# list1=[1,3,5,7,9,10]
# list2=[2,4,6,8]
# result=list1[:-1]+list2
# print("Expected output:",result)

''' 2. Write a Python program to check whether the n-th element exists in a given list.'''

# sample_list=[10,20,30,40,50]
# n=3
# if n<len(sample_list):
#     print(f"{n}-th element exists:{sample_list}")
# else:
#     print(f"{n}-th element does not exist in the list.")

''' 3. Write a program to create a list of empty dictionary'''

# n=5
# empty_dict_list=[{} for _ in range(n)]
# print("List of empty dictionaries:",empty_dict_list)

'''4. Write a Python program to reverse a given list of lists'''

# input_list=[[1,2,3],[4,5,6],[7,8,9]]
# reversed_list=[sublist[::-1] for sublist in input_list[::-1]]
# print(reversed_list)


''' 5. Write a Python program to remove specific words from a given list.
 Original list:
 ['red', 'green', 'blue', 'white', 'black', 'orange']
 Remove words:
 ['white', 'orange']
 After removing the specified words from the said list:
 ['red', 'green', 'blue', 'black']'''

# original_list=['red','green','blue','white','black','orange']
# removed_word=['white','orange']
# filtered_list=[word for word in original_list if word not in removed_word]
# print(filtered_list)


'''6 .Write a Python program to combine two lists into another list randomly.'''

# import random
# list1=[1,2,3,4,5]
# list2=['a','b','c','d','e']
# combined_list=list1+list2
# random.shuffle(combined_list)
# print(combined_list)

'''7.write a program to check whether entered number is Fibonacci number or not'''

# import math
# def isPerfectSquare(x):
#     s=int(math.sqrt(x))
#     return s*s==x
# def isFibonacci(n):
#     return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)
# i = int(input("Enter the number:"))
# if (isFibonacci(i)==True):
#     print(i,"is a Fibonacci Number")
# else:
#     print(i,"is a not Fibonacci Number")



'''8.write a program to check whether entered number is Fibonacci number or not in range '''

# import math
# def isPerfectSquare(x):
#     s=int(math.sqrt(x))
#     return s*s==x
# def isFibonacci(n):
#     return isPerfectSquare(5*n*n+4) or isPerfectSquare(5*n*n-4)
# a = int(input("Enter the terms:"))
# for i in range(1,a):
#     if (isFibonacci(i)==True):
#         print(i,"is a Fibonacci Number")
#     else:
#         print(i,"is a not Fibonacci Number")


'''Use of else with loops'''

# l=[1,2,3,4,5]
# for a in l:
#     print(a)
# else:
#     print("else block is executed:")


i=0
while i<5:
    i+=1
    print("i =",i)
else:
    print("else block is executed:")
    

