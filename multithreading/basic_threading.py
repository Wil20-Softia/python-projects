import threading
import time

ls = []

def count(n):
    for i in range(1, n+1):
        ls.append(i)
        time.sleep(0.5)

def count2(n):
    for i in range(1, n+1):
        ls.append(i)

x = threading.Thread(target=count, args=(5,))
x.start()

y = threading.Thread(target=count, args=(5,))
y.start()

x.join()
y.join()

print(ls)