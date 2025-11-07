'''Write a python program to create an array of 5 random integer between 10 and 50(inclusive 10 
and 50)'''

# import numpy as np
# random_integer=np.random.randint(10,51,size=5)
# print(random_integer)


'''Write a NumPy program to shuffle numbers between 0 and 10 (inclusive).'''

# import numpy as np
# numbers=np.arange(11)
# np.random.shuffle(numbers)
# print(numbers)


'''Write a NumPy program to create a 3x3x3 array with random values'''
# import numpy as np
# random_array=np.random.random((3,3,3))
# print(random_array)


# import pandas as pd
# data=[1,2,3,4]
# ser=pd.Series(data)
# print(ser)


'''Creating series from list'''


# import pandas as pd
# list=['h','e','l','l','o']
# ser=pd.Series(list)
# print(ser)


''' Accessing Element from Series with Position'''

# import pandas as pd
# import numpy as np
# data=np.array(['l','e','e','m'])
# ser=pd.Series(data)
# print(ser[:2])


'''Accessing Element Using Label (index)'''

# import pandas as pd
# import numpy as np
# data=np.array(['p','y','t','h','o','n','o','u','n','i','t','5','s'])
# ser=pd.Series(data,index=[10,11,12,13,14,15,16,17,18,19,20,21,22])
# print(ser[16])


'''Binary operator'''

# import pandas as pd
# data=pd.Series([5,2,3,7],index=['a','b','c','d'])
# data1=pd.Series([1,6,4,9],index=['a','b','d','e'])
# print(data.add(data1,fill_value=0))
# print(data.sub(data1,fill_value=0))


'''Create a Pandas DataFrame from dictionary'''

# import pandas as pd
# data={'Name':['Tom','nick','krish','jack'],
#       'Age':[20,21,19,18]}
# df=pd.DataFrame(data)
# print(df)


'''Create a Pandas DataFrame from dictionary'''
# import pandas as pd
# data={'Name':['Jai','Princi','Guarav','Anuj'],
#       'Age':[27,24,22,32],
#       '      Address':['Delhi','Kanpur','Allahabad','Kannauj'],
#       '      Qualification':['Msc','MA','MCA','Phd']}

# df=pd.DataFrame(data)
# print(df)
# print(df[['Name','Age']])



''''Write a Pandas program to compare the elements of the two Pandas Series. Sample Series: [2, 4, 6, 
8, 10], [1, 3, 5, 7, 10]'''

# import pandas as pd
# series1 = pd.Series([2,4,6,8,10])
# series2 = pd.Series([1,3,5,7,10])
# comparision_result=series1=series2
# print(comparision_result)


'''Write a Pandas program to sort a given Series.'''

import pandas as pd
series = pd.Series([10,2,5,8,1,7])
sorted_seriues=series.sort_values()
print("Sorted sereis in ascending order:")
print(sorted_seriues)