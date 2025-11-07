''' Open afile the to read the content'''

# file = open("sales.txt","r+")
# content=file.read()
# print(content)
# file.close()

with open("sales.txt","r+") as file:
 content=file.read()
 print(content)
 file.close()