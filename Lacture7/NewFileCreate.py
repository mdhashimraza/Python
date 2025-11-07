with open("Practics.txt","r")as f:
#    data = f.read()
#    print(data)
#    new_data = data.replace("Java","Python")
#    print(new_data)

# with open("Practics.txt","w")as f:
#   f.write(new_data)


word = "learning"
with open("Practics.txt","r"):
   data = f.read()
   if(data.find(word) != -1):
     print("Found")
   else:
     print("Not Found")