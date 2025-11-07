class A:
    varA = "welcom to class A"

class B:
    varB = "welcom to class B"

class C(A,B):
    varC = "welcom to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)