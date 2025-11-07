'''1. Write a Python program to count the number of elements in a list within a specified range.'''

# number=[5,15,3,8,9,12,20,25,30]
# lower_bound=10
# upper_bound=15
# count_in_range=sum(1 for num in number if lower_bound <= num <= upper_bound)
# print(f"Number of element in the list within the range {lower_bound} to {upper_bound} : {count_in_range}")


''' 2. Write a Python program to check whether a list contains a sub list.'''

# mail_list=[1,4,5,6,7,8,9]
# sub_list=[4,5,6]
# found=False
# for i in range(len(mail_list)-len(sub_list)+1):
#     if mail_list[i:i+len(sub_list)]==sub_list:
#         found=True
#         break
# if found:
#     print("The main list contain the sublist.")
# else:
#     print("The main list does not contain the sublist.")


'''3. Write a Python program to find common items in two lists'''

# list1=[1,2,3,4,5,6,7]
# list2=[3,4,5,6,7,8,9]
# common_item=[]
# for item in list1:
#     if item in list2:
#         common_item.append(item)
# print("Common item :",common_item)


''' 4. Write a Python program to convert a list of multiple integers into a single integer.'''

# list1=[1,23,456,7,89]
# result_string=""
# for num in list1:
#     result_string += str(num)
# single_integer = int(result_string)
# print("The single integer is :",single_integer)

'''5. Write a Python program to split a list based on the first character of a word.'''

# words=['apple','banana','apricot','blueberry','cherry','date','fig','grape']
# split_dict={}
# for word in words:
#     first_char=word[0]
#     if first_char not in split_dict:
#         split_dict[first_char]=[]
#     split_dict[first_char].append(word)
# for char,word_list in split_dict.items():
#     print(f"Word starting with '{char}' : {word_list}")


''' 6. Write a Python program to create multiple lists.'''

# list1=[1,2,3]
# list2=['a','b','c']
# list3=[True,False,True]
# list4=[3.14,2.71,1.41]
# multiple_list=[list1,list2,list3,list4]
# print("List 1:",list1)
# print("List 2:",list2)
# print("List 3:",list3)
# print("List 4:",list4)
# print("Multiple list:",multiple_list)


'''7. Write a Python program to split a list into different variables.'''

# my_list=[10,20,30,40,50]
# var1,var2,var3,var4,var5=my_list
# print("Variable 1:",var1)
# print("Variable 2:",var2)
# print("Variable 3:",var3)
# print("Variable 4:",var4)
# print("Variable 5:",var5)


''' 8. Write a Python program to insert an element before each element of a list.'''

# original_list=[10,20,30,40,50]
# element_to_insert='X'
# modified_list=[]
# for item in original_list:
#     modified_list.append(element_to_insert)
#     modified_list.append(item)
# print("Modified list:",modified_list)


'''9. Write a Python program to split a list every Nth element.
Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]'''

# sample_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
# N=3
# split_list=[]
# for i in range(N):
#     sublist=sample_list[i::N]
#     split_list.append(sublist)
# print("Resulting split list:")
# print(split_list)


'''10. Write a Python program to concatenate elements of a list.'''

# string_list=['Hello','World','From']
# concatenated_string=' '.join(string_list)
# print("Concatenated string:",concatenated_string)

''' 11.. Write a Python program to convert a string to a list.'''

# input_string="Hello, world"
# result=list(input_string)
# print(result)


''' 12.. Write a Python program to check if all items in a given list of strings are equal to a given 
string.'''

string_list=['apple','apple','apple']
target_string="apple"
all_equal=all(item==target_string for item in string_list)
print("All item are equal to the target string :",all_equal)





