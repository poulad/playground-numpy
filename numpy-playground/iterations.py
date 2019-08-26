import numpy as np

a_random = np.array(np.floor(np.random.random((2, 4)) * 35))

print(f"Randomly generated array:\n{a_random}")
print(f"Reversed:\n{a_random[::-1]}")

a_func = np.fromfunction(lambda x, y: 2 * x + y, (4, 6), dtype=np.int16)
print(f"2x+y:\n{a_func}")

print(f"its 3rd column is: {a_func[:, 2]}")
print(f"2nd and 4th rows are:\n{a_func[1:4:2, :]}")

print("array elements are: [ ", end="")
for el in a_func.flat:
    print(f"{el}, ", end='')
else:
    print("]")
