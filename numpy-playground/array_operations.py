import numpy as np

a_random = np.array(np.floor(23 * np.random.random((3, 4))))
print(f"randomly-generated array is:\n{a_random}")

print(f"min element in each column: {a_random.min(axis=0)}")
print(f"max element in each row: {a_random.max(axis=1)}")

print(f"cumulative sum for each row:\n{a_random.cumsum(axis=1)}")

a_angles = 90 * np.arange(7)
print(f"a_angles array is\n{a_angles}")
print(f"their sins are:\n{np.sin(a_angles)}")
