import numpy as np

a = np.arange(15)
a.shape = 3, 5
print(
    "Array A:", a,
    f"\twith ID of {id(a)}",
    sep="\n##################\n"
)

# shallow copy
b: np.ndarray = a[:, 3:5]  # slicing is shallow copy
print(f"Sliced array B(shallow copy):\n{b}")
print(f"B is a view of A. {b.base is a}")
print(f"B has the following flags:\n{b.flags}")

# deep copy
c: np.ndarray = a[:, 3:5].copy()
del a  # release the memory of A

print(f"C is a deep copy of A:\n{c}")
