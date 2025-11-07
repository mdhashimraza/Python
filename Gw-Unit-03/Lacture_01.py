# l1=[]
# print(l1)
# l2=[1,2,3,4]
# print(l2)
# l3=[1,2,3.5,4,'Hello']
# print(l3)
# l4=[1,2,3,3,3,3,2,2,2,2,4.4,5,5,5,5,4]
# print(l4)
# l5=[1,2,3]
# l5[2]=99
# print(l5)


'''LIST METHODS'''

# l=[1,7,2,8,4,5]

# l.append(6)
# print(l)

# print(max(l))

# print(min(l))

# l.reverse()
# print(l)

# print(l.sort())
# l.sort()
# print(l)

# l.sort(reverse=True)
# print(l)

# l.remove(5)
# print(l)

# print(l.pop(4))
# print(l)

# print(l.pop())
# print(l)

# l.insert(2,'Hashim')
# print(l)

# print(l.index('Hashim'))

# print(l.count('Hashim'))

# l.clear()
# print(l)

# l1=[8,9,7,5,6,4,8]
# l.extend(l1)
# print(l)


# import copy
# original=[4,3,[1,2],5,6]
# # shallow_copy=copy.copy(original)
# shallow_copy=copy.deepcopy(original)
# print(original)
# print(shallow_copy)
# shallow_copy[1]=99
# print(shallow_copy)
# shallow_copy[2][0]=88
# print(shallow_copy)


''' TO PRINT THE COMPLETE LIST'''
# l=[50,60,70,80,90,40,3,0]
# print(l[::])
# print(l[-8::1])
# print(l[1:5])
# print(l[1:8:3])


'''1 Print from 4 element of the list then take
 jump of 2uptothe end ofthe list.'''

# l=[1,2,3,4,5,6,7,8,9]
# print(l[3:9:2])
# print(l[::2])


''' Write a function to find ASCII value of the character.'''

# def ascii_value(a):
#     print(ord(a))
# ascii_value('A')

'''Write a program to reverse a list'''

# l=[1,2,3,4,5]
# reversed_l=l[::-1]
# print(reversed_l)

'''List comprehension'''

# l=[5,4,6,2,8]
# double=[x*2 for x in l]
# print(l)
# print(double)

# list=[i+3 for i in range(11) if i%2==0]
# print(list)

'''Question:- Write a function lessthan (lst,k) to return 
list of number less than k from the list  lst. The 
function mnust use list comprehension  
Lessthan([1,-2,0,5,-3],0) returns[-2.-3] (AKTU 2020
21)'''

# def lessThan(lst,k):
#     return[i for i in lst if i<k]
# print(lessThan([1,-2,0,5,-3],0))


'''lustrate different list slicing constructs for
 the following operations on the following
 list:L= [1, 2, 3, 4, 5, 6, 7, 8, 9]
 (AKTU 2023-24ODD)
 1. Return a list of numbers starting from
 the last to second item of the list
 2.
 Return a list that start from 3rd item
 to second last item.
 3.
 4.
 5.
 Return a list that has only even
 position elements of list L.
 Return a list that starts from the
 middle of the list L.
 Return a list that reverses all the
 elements starting from element at
 index 0 to middle index only and
 return the entire list.
 6. Divide each element of the list by 2
 and replace it with the remainder.'''

list=[1,2,3,4,5,6,7,8,9]
# 1 solution
result1=list[::-1][:-1]
print(result1)
# 2 solutoin
result2=list[2:-1]
print(result2)
# 3 solution
result3=list[0::2]
print(result3)
# 4 solution
middle=len(list)//2
result4=list[middle:]
print(result4)
# 5 solution
result5=list[:middle+1][::-1][middle+1:]
print(result5)
# 6 solution
result6=[x%2 for x in list]
print(result6)








