import numpy as np

# Create an int8 array
arr = np.array([1, -1, 127, -128], dtype=np.int8)

# Convert to bytes
byte_representation = arr.tobytes()

print(byte_representation)
