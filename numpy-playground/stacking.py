import numpy as np
from numpy import newaxis

a = np.array(np.floor(np.random.random((2, 2)) * 56), dtype=np.int16)
b = np.array(np.ceil(np.random.random((2, 2)) * 49), dtype=np.int16)
print(f"Array a\n:{a}")
print(f"Array b\n:{b}")

print(
    "Horizontal stack:", np.hstack((a, b)),
    "Vertical stack:", np.vstack((a, b)),
    sep="\n"
)

c = np.arange(1, stop=6, step=2)
print(f"Array C:\n{c}")
# add a new axis to it
print(f"Reshaping C into a 3x1 matrix:\n{c[:, np.newaxis]}")
print(f"Reshaping C into a 1x3 matrix:\n{c[newaxis, :]}")

d = np.array(np.floor(np.random.random((4, 5)) * 57), dtype=np.int16)
print(f"Array d:\n{d}")
print(f"split into 3 arrays horizontally between 2nd and 3rd columns:\n{np.hsplit(d, (1, 2))}")

