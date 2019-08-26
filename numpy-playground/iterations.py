import numpy as np

a_random = np.array(np.floor(np.random.random((2, 4)) * 35))

print(f"Randomly generated array:\n{a_random}")
print(f"Reversed:\n{a_random[::-1]}")

a_func = np.fromfunction(lambda x, y: 2 * x + y, (3, 5))
print(f"2x+y:\n{a_func}")

print(f"its 3rs column is: {a_func[:, 2]}")
