class MyClass():

    def __init__(self):
        pass

    def __str__(self):
        return 'meow'

    def __len__(self):
        return 100

    def __del__(self):
        print('reclaimed')

if __name__ == '__main__':
    my_obj = MyClass()
    print(str(my_obj))
    print(len(my_obj))
    del my_obj
    
