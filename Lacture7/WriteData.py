f =  open("sample.txt","a+")
f.write("abc ")
print(f.read())
f.write(" \nI want to learn c++ programming language")
f.close
f = open("sample.txt","a")
