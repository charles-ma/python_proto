def compre():
    l = [1, 2, 3]
    d = {x:x for x in l if x > 1}
    n = [x**2 for x in l if x > 0]
    s = {x*5 for x in l if x > 2}

    print(d)
    print(n)
    print(s)

if __name__ == '__main__':
    compre()
