class persion:
    __name = "anonymous"

    def __hello(self):
        print("Hello Persion!")

    def welcom(self):
        self.__hello()

p1 = persion()

print(p1.welcom())