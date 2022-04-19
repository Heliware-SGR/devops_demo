import random
import time
def demo_in():
    time.sleep(2)
    a = random.randint(0,10)
    if a == 5:
        return 12
    else:
        return a
r = demo_in()
print(r)
