import numpy as np

a_random = np.array(np.floor(10 * np.random.random((2, 4))))

print(f"our 2x4 matrix is:\n {a_random}")

print(f"its transposed matrix is:\n {a_random.T}")

# trying to auto-reshape it into 3 rows
a_reshaped = None
try:
    a_reshaped = a_random.reshape((3, -1))
except ValueError as e:
    if e.args[0].startswith('cannot reshape array'):
        print(f"Failed to reshape the array. {e.args[0]}")
    else:
        raise e

if a_reshaped:
    print(f"new reshaped form of it:\n{a_reshaped}")
