def sum_dec(f):
    def wrapper(x, y):
        f(x, y)
        print(f'the sum is {x + y}')
    return wrapper

def sub_dec(f):
    def wrapper(x, y):
        f(x, y)
        print(f'the diff is {x - y}')
    return wrapper

@sub_dec
@sum_dec
def echo(x, y):
    print(f'received {x}, {y}')

if __name__ == '__main__':
    echo(1, 2)
