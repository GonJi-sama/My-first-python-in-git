import numpy as np
from my0677 import gong as fx

num_1 = []
num_2 = []

for _ in range(10):
    num_1.append(np.random.randint(1, 100))
    num_2.append(np.random.randint(1, 100))

fx.myfunc(num_1, num_2)