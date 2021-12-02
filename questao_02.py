import time

for k in range(10, -1, -1):
    print(k)
    time.sleep(1)
    if k == 0:
        print("Fogo!")