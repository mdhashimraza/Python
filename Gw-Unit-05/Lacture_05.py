'''Tkinter
 Python Tkinter is a standard GUI (Graphical User Interface) library for Python which provides a
 fast and easy way to create desktop applications.
 Tkinter provides a variety of widgets like buttons, labels, text boxes, menus and more that can
 be used to create interactive user interfaces.'''

# import tkinter as tk
# m= tk.Tk()
# m.mainloop()


'''Tkinter Widget'''

# from tkinter import *
# root= Tk()
# w= Label(root,text='Hello Hashim')
# w.pack()
# root.mainloop()



'''Tkinter Widget'''

# from tkinter import *
# root= Tk()
# w= Label(root,text='Hello',font=('Arial',50,"bold"),fg='red',bg='yellow',width=20,height=2)
# w.pack()
# root.mainloop()


'''  1.Button
 a Button is a widget that users can click to perform an action, such as closing a window, running a function, or opening
 another window'''

# import tkinter as tk
# r= tk.Tk()
# r.title('Counting second')
# button=tk.Button(r,text='Stop',width=10,height=2,command=r.destroy,bg='skyblue',fg='white',font=('Arial',14,'bold'))
# button.pack()
# r.mainloop()


'''3.Entry
 The Entry widget in Tkinter is used to create a single-line text input field where users can
 type and edit text. It's commonly used in forms or dialogs to capture user input.
 Entry(master, options)'''

# from tkinter import *
# master=Tk()
# Label(master,text='First name').grid(row=0)
# Label(master,text='Middle name').grid(row=1)
# Label(master,text='Last name').grid(row=2)
# # Label(master,text='First name').grid(column=0,row=0)
# # Label(master,text='Middle name').grid(column=2,row=0)
# # Label(master,text='Last name').grid(column=4,row=0)
# e1=Entry(master)
# e2=Entry(master)
# e3=Entry(master)
# # e1.grid(row=0,column=1)
# # e2.grid(row=0,column=3)
# # e3.grid(row=0,column=5)
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)
# e3.grid(row=2,column=1)
# mainloop()


'''Checkbutton'''

# from tkinter import *
# master=Tk()
# var1=IntVar()
# Checkbutton(master,text='Male',variable=var1).grid(row=0,sticky=W)
# var2=IntVar()
# Checkbutton(master,text='Female',variable=var2).grid(row=1,sticky=W)
# mainloop()


'''Radiobutton'''

# from tkinter import *
# master=Tk()
# gender=IntVar()
# Radiobutton(master,text='Male',variable=gender,value=1).grid(row=0,sticky=W)
# Radiobutton(master,text='Female',variable=gender,value=2).grid(row=1,sticky=W)
# mainloop()






