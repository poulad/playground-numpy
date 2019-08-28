import numpy as np

a: np.ndarray = (np.arange(12) ** 2).reshape(3, 4)
print(f"A is:\n{a}")

# setting elements using array indexes
a[[0, 1], [2, 3]] = [5, 55]
print(f"Edited:\n{a}")
