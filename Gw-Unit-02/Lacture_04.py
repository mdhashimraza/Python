''' 1. Write a Python program to remove
 duplicates from a list.'''

# a=[1,2,2,3,4,5,5,3]
# unique=list(set(a))
# print("Duplicates remove:",unique)


''' 2. Write a Python program to check if a list is 
empty or not.'''

# a=[]
# if not a:
#     print("List is empty")
# else:
#     print("List is not empty")


'''3. Write a Python program to clone or copy a list'''

# list=[1,2,3,4,5,6]
# copied_list=list.copy()
# print("Original list:",list)
# print("Copied list:",copied_list)


''' 4.Write a Python program to find the list of 
words that are longer than n from a given list of 
words'''

# word=['Apple','Banana','Cherry','Orange','Date','Grape']
# n=5
# long_word=[x for x in word if len(x)>n]
# print("Word longer than",n, "charector:",long_word)


'''5.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
 Sample List : ['Red','Green','White','Black', 'Pink','Yellow']
  Expected Output : ['Green', 'White', 'Black']'''

# sample_list=['Red','Green','White','Black','pink','Yellow']
# result=[sample_list[i] for i in range(len(sample_list)) if i not in (0,4,5)]
# print("Expected output",result)

''' 6. Write a Python program to print the numbers of a specified list after removing even
 numbers from it'''

# numbers=[1,2,3,4,5,6,7,8,9,10]
# odd_numbers=[num for num in numbers if num%2 !=0]
# print("List after removing even number:",odd_numbers)


'''7. Write a Python program to shuffle and print a specified list'''

# import random as n
# sample_list=[1,2,3,4,5,6,7,8,9,10]
# n.shuffle(sample_list)
# print("Shuffled list:",sample_list)

''' 8. Whose number square is less than equal to 30 range is taken between 1 to 30'''

# square_numner=[i**2 for i in range(1,31) if i**2<=30]
# print(square_numner)
# first_five=square_numner[:5]
# last_five=square_numner[-5:]
# print("First 5 squre number:",first_five)
# print("Last 5 squre number:",last_five)


'''9. Write a Python program to check if each
 number is prime in a given list of numbers.
 Return True if all numbers are prime otherwise
 False.'''

# numbers=[2,3,5,7,11]
# all_prime=True
# for num in numbers:
#     if num<2:
#         all_prime=False
#         break
#     for i in range(2,num):
#         if num%i ==0:
#             all_prime=False
#             break
# print("All numbers are prime:",all_prime)


'''10.Write a Python program to calculate the
 difference between the two lists.'''

# list1=[1,2,3,4,5]
# list2=[4,5,6,7,8]
# difference=[item for item in list1 if item not in list2]
# print("Difference the between two list",difference)


'''11. Write a Python program to access the
 index of a list.'''

# nums=[5,15,35,8,98]
# for num_index,num_value in enumerate(nums):
#     print(num_index,num_value)


''' 12. Write a Python program to convert a list of
 characters into a string.'''

# char_list=['H','e',' ','w','o']
# result_string=''.join(char_list)
# print("Converted string:",result_string)


'''13. Write a Python program to find the index of an
 item in a specified list.'''

# sample_list=['Apple','Banana','Cherry','Data','Orange']
# item_to_find='Cherry'
# if item_to_find in sample_list:
#     index=sample_list.index(item_to_find)
#     print(f"The index of {item_to_find} is:{index}")
# else:
#     print(f"{item_to_find} is not in the list")


'''14. Write a Python program to append a list to the
 second list.'''

# list1=[1,2,3]
# list2=[4,5,6]
# list2.extend(list1)
# print("Modified second list",list2)


'''15. Python program to find the second smallest 
number in a list:'''

# numbers=[5,15,3,8,9,12]
# unique_number=list(set(numbers))
# unique_number.sort()
# if len(unique_number)>=2:
#     second_smallest=unique_number[1]
#     print("The second smallest number is:",second_smallest)
# else:
#     print("There is no second smallest number.")


'''16 . Python program to find the second largest
 number in a list:'''

# numbers=[5,15,3,8,9,12]
# unique_number=list(set(numbers))
# unique_number.sort(reverse=True)
# if len(unique_number)>=2:
#     second_largest=unique_number[1]
#     print("The second largest number is:",second_largest)
# else:
#     print("There is no second largest number.")



'''17. Write a Python program to get unique values from a list.'''

# numbers=[1,2,3,2,4,5,1,6,4]
# unique_value=list(set(numbers))
# print("The unique value in the list:",unique_value)


''' 18.Write a Python program to get the frequency of elements in a list'''

elements=['Apple','Banana','Apple','Orange','Banana','Apple']
frequency={}
for item in elements:
    if item in frequency:
        frequency[item] +=1
    else:
        frequency[item]=1
print("Frequency of elements in the list:")
for item,count in frequency.items():
    print(f"{item}:{count}")




