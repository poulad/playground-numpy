import numpy as np

a: np.ndarray = np.arange(15).reshape(3, 5)
print(f"Data type is {a.dtype}")

b = np.empty((2, 3), np.int32)
print(b)

a_linspace = np.linspace(0, 2 * np.pi, 20)
print(np.sin(a_linspace))

a_random: np.ndarray = np.floor(10 * np.random.random((3, 3)))

print(f"a_random array is: \n{a_random}")
print(f"falttened: {a_random.ravel()}")
print(f"transposed: \n {a_random.T}")

a_random.resize((4, 5))
print(f"a_random array resized:\n{a_random}")
