'''Visualizing data helps us understand and share information more effectively.
  InPython , Matplotlib is one of the best tools for creating visualizations.
 Different types of plolt
 1.Line plot
 2.Bar plot
 3.Pie chart
 4.Scatter plot
 5.Histogram'''

'''Bar plot
 Adjusting Bar Width
Customizing Bar Colors'''

# import matplotlib.pyplot as plt
# fruits=['Apple','Banana','Orange','Date']
# sales=[400,350,300,450]
# plt.bar(fruits,sales,color='pink',width=0.5)
# plt.title('Fruit Sales')
# plt.xlabel('Fruits')
# plt.ylabel('Sales')
# plt.show()


'''piechart'''

# import matplotlib.pyplot as plt
# cars=['AUDI','BMW','FORD','TESLA','JAGUAR','MERCEDES']
# data=[23,17,35,29,12,41]
# fig=plt.figure(figsize=(10,7))
# plt.pie(data,labels=cars)
# plt.show()


# import matplotlib.pyplot as plt
# x=[1,2,3,4,5]
# e=[0.1,0,0,0,0]
# plt.pie(x,explode=e)
# plt.title('Pie Chart')
# plt.show()

'''Matplotlib Scatter'''
'''Scatter Plot with Multiple Datasets'''

# import matplotlib.pyplot as plt
# import numpy as np
# x1=np.array([12,45,7,32,89,54,23,67,14,91])
# y1=np.array([100,95,85,75,65,45,35,25,15,5])
# x2=np.array([10,12,15,17,16,25,24,45,56,55,59])
# y2=np.array([5,10,15,20,25,30,35,40,45,50,55])
# plt.scatter(x1,y1,color='blue',label='Group 1')
# plt.scatter(x2,y2,color='red',label='Group 2')
# plt.xlabel('Height (cm)')
# plt.ylabel('Weight (Kg)')
# plt.title('Comparision of Height vs Weight between two groups ')
# plt.legend()
# plt.show()



'''Different Types of Plots
 1. Line chart'''

# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([1,2,3,4])
# y=x*2
# plt.xlabel('X-axis')
# plt.ylabel('Y-axis')
# plt.title('Any suitable title')
# plt.plot(x,y,'-.',color='r')
# plt.show()


'''Different Types of Plots
 Multiple Plots on the Same Axis'''



# import matplotlib.pyplot as plt
# import numpy as np
# x=np.array([1,2,3,4])
# y=x*2
# x1=[2,4,6,8]
# y1=[3,5,7,9]
# plt.xlabel('X-axis data')
# plt.ylabel('Y-axis data')
# plt.title('Multiple plots')
# plt.plot(x,y,'-.',color='r',label='Level 1')
# plt.plot(x1,y1,color='g',label='Level 2')
# plt.legend()
# plt.show()


'''Histogram'''

# import matplotlib.pyplot as plt
# data=[2,3,57,8,9,11,13,14,15,17,18,19,20]
# plt.figure(figsize=(12,6))
# plt.subplot(1,2,1)
# plt.hist(data,bins=4,color='skyblue',edgecolor='black')
# plt.xlabel('Value Range')
# plt.ylabel('Frequency')
# plt.title('Histogram with bins=4')

plt.subplot(1,2,2)
plt.hist(data,bins=6,color='lightgreen',edgecolor='black')
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.title('Histogram with bins=6')
plt.tight_layout()
plt.show()