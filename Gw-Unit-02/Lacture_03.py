
# Patern

# rows=5
# for i in range(1,rows+1):
#     print("* "*i)


# rows=5
# for i in range(rows,0,-1):
#     print("* "*i)


# rows=5
# for i in range(1,rows+1):
#     print(' '.join(str(x) for x in range(1,i+1)))


# rows=5
# for i in range(rows,0,-1):
#     print(' '.join(str(x) for x in range(1,i+1)))


# rows=5
# for i in range(1,rows+1):
#     print(' '.join(chr(64+i) for _ in range(i)))


# rows=5
# for i in range(rows,0,-1):
#     print(' '.join(chr(64+i) for _ in range(i)))


# rows=5
# for i in range(1,rows+1):
#     print('  '*(rows-i)+'* '*(2*i-1))


# rows=5
# for i in range(rows,0,-1):
#     print('  '*(rows-i)+'* '*(2*i-1))




# rows=5
# for i in range(1,rows+1):
#     print('  '*(rows-i)+'* '*(2*i-1))
# for i in range(rows-1,0,-1):
#     print('  '*(rows-i)+'* '*(2*i-1))


'''1. Write a Python script to add a key to a dictionary'''

# my_dic={0:10,1:20}
# my_dic[2]=30
# print("Upfated dictionary: ",my_dic)


''' Write a Python script to concatenate/merge the
 following dictionaries to create a new one.'''

# dict1={1:10,2:20}
# dict2={3:30,4:40}
# dict3={5:50,6:60}
# dict4={7:70,8:80}
# new_dict={}
# for d in (dict1,dict2,dict3,dict4):
#     new_dict.update(d)
# print("Concatenated dictionary: ",new_dict)


'''3. Write a Python script to check whether a given key already exists in a 
dictionary.'''

# my_dic={1:10,2:20,3:30,4:40}
# key=3
# if key in my_dic:
#     print("Yes")
# else:
#     print("No")


'''4.Write a Python program to iterate over dictionaries using for loops'''

# dict={'apple':10,'banana':20,'cherry':30}
# print("Keys:\n")
# for key in dict:
#     print(key)
# print("\nValues:\n")
# for value in dict.values():
#     print(value)
# print("\nKey-Value Pairs:\n")
# for key,value in dict.items():
#     print(f"{key}:{value}")



'''5. Write a Python script to generate and print a dictionary that contains
 a number (between 1 and n) inthe form (x, x*x).'''

# n=int(input("Enter the any number: "))
# squared_dict={x:x*x for x in range(1,n+1)}
# print("Generated dictionary: ",squared_dict)



''' 6.Write a Python script to print a dictionary where the keys are numbers
 between 1and15(bothincluded) and the values are the square of the keys.'''

# squared_dict={x:x*x for x in range(1,16)}
# print("Generated dictionary: ",squared_dict)


'''7. Write a Python program to sum all the items in a dictionary'''

# my_dic={'a':10,'b':20,'c':30}
# total_sum=sum(my_dic.values())
# print("Total sum of values:",total_sum)


'''8.Write a Python program to Multiply all the items in a dictionary'''

# my_dic={'a':10,'b':20,'c':30}
# result=1
# for value in my_dic.values():
#     result*=value
# print("Product of all values:",result)



''' 9. Write a Python program to remove a key from a dictionary.'''

# my_dic={'a':10,'b':20,'c':30}
# key_remove='b'
# if key_remove in my_dic:
#     del my_dic[key_remove]
# print("Updated dictionary:",my_dic)



'''10.Write a Python program to map two lists into a 
dictionary.'''

# keys=['a','b','c']
# values=[1,2,3]
# mapped_dic=dict(zip(keys,values))
# print("Mapped dictionary:",mapped_dic)


'''11 Write a Python program to sort a given 
dictionary by key.'''

# my_dic={'banana':2,'grapes':1,'cherry':3}
# sorted_dic=dict(sorted(my_dic.items()))
# print("Dictionary sorted by keys:",sorted_dic)


''' 12. Write a Python program to get the maximum and
 minimumvaluesof a dictionary.'''

# my_dic={'a':10,'b':20,'c':30,'d':5}
# max_value=max(my_dic.values())
# min_value=min(my_dic.values())
# print("Maximum value:",max_value)
# print("Minimum value:",min_value)


'''13. Write a Python program to remove 
duplicates from the dictionary.'''

# my_dic={'a':10,'b':20,'c':10,'d':30,'e':20}
# unique_dic={}
# for key,value in my_dic.items():
#     if value not in unique_dic.values():
#         unique_dic[key]=value
# print("Dictionary without duplicate:",unique_dic)


''' 14 Write a Python program to check if a 
dictionary is empty or not.'''

# my_dic={}
# if my_dic:
#     print("The dictionary is not empty.")
# else:
#     print("The dictionary is empty.")


''' 15. Write a Python program to combine two
 dictionary by adding values for common keys.
 d1 = {'a':100,'b':200,'c':300}
 d2 = {'a':300,'b':200,'d':400}
 Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c':300})'''
 
# from collections import Counter
# d1 = {'a':100,'b':200,'c':300}
# d2 = {'a':300,'b':200,'d':400}
# combined_dic=Counter(d1)+Counter(d2)
# print("Combined dictionary:",combined_dic)


'''16.Writea Pythonprogram
 toprintalldistinctvalues in
 a dictionary.
 SampleData: [{"V":"S001"},
 {"V":"S002"}, {"VI":"S001"},
 {"VI": "S005"},
 {"VII":"S005"},
 {"V":"S009"},{"VIII":"S007"}]
 Expected Output : Unique
 Values: {'S005', 'S002',
 'S007','S001','S009'}'''

data=[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},
      {"V":"S009"},{"VIII":"S007"}]
distinct_value=set()
for dictionary in data:
    distinct_value.update(dictionary.values())
print("Distinct value:",distinct_value)


'''17 18 19 20 21 22 23 24 25 26 question baki'''




