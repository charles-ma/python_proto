import threading

def infinite_loop():
    while True:
        pass

'''
if we spin up two running processes without threads, will consume 2 cpu cores
cpu usages of multiple threads always add up to ~100%
'''
if __name__ == '__main__':
    t1 = threading.Thread(target=infinite_loop)
    t2 = threading.Thread(target=infinite_loop)
    t3 = threading.Thread(target=infinite_loop)

    t1.start()
    t2.start()
    t3.start()
    infinite_loop()
