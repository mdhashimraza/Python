# import numpy as np
# arr=np.array([[1,2,3],
#               [4,5,6]])
# print("Array:",arr)
# print("Array is of type:",type(arr))
# print("No of dimention:",arr.ndim)
# print("Shape of array:",arr.shape)
# print("Size of array:",arr.size)
# print("Array store element of type:",arr.dtype)

'''NumPyBasic Operations
 1. Operations on a single NumPy array'''

# import numpy as np
# a=np.array([1,2,3,4,5])
# print("Adding 1 to every element: ",a+1)
# print("Subtract 2 to every element: ",a-2)
# print("multiplying 10 to every element: ",a*10)
# print("Squaring each element: ",a**2)
# print("Double each element of original array:",a*2)
# a=np.array([[1,2,3],[3,4,5],[6,7,8]])
# print("\nOriginal array\n",a)
# print("\nTranspose\n",a.T)


'''NumPy–Unary Operators
 Many unary operations are provided as a method of ndarray class. This includes sum, min, max, 
etc. These functions can also be applied row-wise or column-wise by setting an axis parameter'''

# import numpy as np
# a=np.array([[1,2,3],
#             [3,4,5],
#             [6,7,8]])
# print("largest element is:",a.max())
# print("Row wise maximum element:",
#                   a.max(axis=1))
# print("Columb wise maximum element:",
#                   a.max(axis=0))
# print("Columb wise minimum element:",
#                   a.min(axis=0))
# print("Sum of all array element:",a.sum())
# print("Comutative sum along each row:\n",
#                   a.cumsum(axis=1))


'''NumPy–Binary Operators
 These operations apply to the array elementwise and a new array is created. You can use all basic arithmetic operators 
like +, -, /, etc. In the case of +=, -=, = operators, the existing array is modified'''

# import numpy as np
# a=np.array([[1,2],
#             [2,3]])
# b=np.array([[4,5],
#             [6,7]])
# print("Array sum:\n",
#       a+b)
# print("Array multiplication:\n",
#       a*b)
# print("Matrix multiplication:\n",
#       a.dot(b))


'''Numpysorting array'''


# import numpy as np
# a=np.array([[1,4,2],
#             [3,4,6],
#             [0,-1,5]])
# print("Array elements in sorted order:\n",np.sort(a,axis=None))
# print("Row wise sorted order:\n",np.sort(a,axis=1))
# print("Columb wise by applying merg-sort:\n",np.sort(a,axis=0,kind='mergesort'))
# print("Columb wise by applying merg-sort:\n",np.sort(a,axis=0))


'''Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy
 array.'''

# import numpy as np
# original_list=[12.22,23.32,100,36.45]
# numpy_array=np.array(original_list)
# print("Original List:",original_list)
# print("One_Dimentional numpy array:",numpy_array)


'''Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.'''

# import numpy as np
# matrix=np.arange(2,11).reshape(3,3)
# print("3x3 Matrix with value ranging from 2 to 10:")
# print(matrix)

'''Write a NumPy program to reverse an array (the first element becomes the last)'''

# import numpy as np
# original_array=np.array([1,2,3,4,5])
# reversed_array=original_array[::-1]
# print("Original array:",original_array)
# print("Reversed array:",reversed_array)


# import numpy as np
# original_array=np.array([1,2,3])
# value_to_append=[4,5,6]
# result_array=np.append(original_array,value_to_append)
# print("Original array:",original_array)
# print("Append array:",result_array)


'''Write a NumPy program to find common values between two arrays.'''

# import numpy as n
# a=n.array([1,2,3,4,5])
# b=n.array([3,4,5,6,7])
# common_value=n.intersect1d(a,b)
# print("Array 1:",a)
# print("Array 2:",b)
# print("Common value:",common_value)


'''Write a NumPy program to get the unique elements of an array.'''

# import numpy as p
# array=p.array([1,2,2,2,3,3,4,5,6,6,6,5,7,8,7,9])
# unique_value=p.unique(array)
# print("Original array:",array)
# print("Unique element:",unique_value)


'''Write a
 NumPy program to find the set difference between two arrays. The set difference will 
return sorted, distinct values in array1 that are not in array2'''

# import numpy as np
# array1=np.array([1,2,3,4,5])
# array2=np.array([3,4,5,6,7])
# set_difference=np.setdiff1d(array1,array2)
# print("Array 1:",array1)
# print("Array 2:",array2)
# print("Set difference:",set_difference)



'''Union of two array'''

import numpy as np
array1=np.array([1,2,3,4,5])
array2=np.array([3,4,5,6,7])
union_array=np.union1d(array1,array2)
print("Array 1:",array1)
print("Array 2:",array2)
print("Union of array 1 and array 2:",union_array)




