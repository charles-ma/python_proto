class Product():
    def __init__(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.brand
        

class Computer():
    def __init__(self, a=0, b=1):
        self.a = a
        self.b = b

    def compute(self):
        return self.a + self.b
    

class Mac(Product, Computer):
    def __init__(self, brand):
        Product.__init__(self, brand)
        Computer.__init__(self)


class ClassLevel():
    count = 0

    def plus(self):
        # self.count += 1
        ClassLevel.count += 1
    
    def show(self):
        print(self.count)


if __name__ == '__main__':
    # inheritance 
    mac = Mac('apple')
    print(mac.compute())
    print(mac.get_brand())

    # class level variable
    l1 = ClassLevel()
    l2 = ClassLevel()

    l1.plus()
    l2.plus()
    l1.show()
    l2.show()
    print(ClassLevel.count)
