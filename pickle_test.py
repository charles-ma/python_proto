import pickle

class Animal():

    def __init__(self, breed):
        self.breed = breed

    def make_sound(self):
        pass

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self, 'dog')

    def make_sound(self):
        print('wong')


if __name__ == '__main__':

    dog = Dog()

    dog.make_sound()
    
    file = open('pickle.pkl', 'wb')
    pickle.dump(dog, file)
    file.close()

    file1 = open('pickle.pkl', 'rb')
    data = pickle.load(file1)
    file1.close()

    print(type(data))
    data.make_sound()

    
