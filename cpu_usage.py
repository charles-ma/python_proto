import threading

def infinite_loop():
    while True:
        pass

'''
if we spin up two running processes without threads, will consume 2 cpu cores
if we spin up processes with threads, each process will still consume 100% cpu with 50% for each thread
'''
if __name__ == '__main__':
    # t1 = threading.Thread(target=infinite_loop)
    # t2 = threading.Thread(target=infinite_loop)

    # t1.start()
    # t2.start()
    infinite_loop()
