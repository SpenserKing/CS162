import numpy as np

# Generate random 5x5 array
array = np.random.randint(23, 847, size=(5, 5))

# Print the array
print("Array:")
print(array)

# Print number from 2nd row, 3rd column
print("\nValue at 2nd row, 3rd column:")
print(array[1][2])

# Print sum of all elements
print("\nSum of all elements:")
print(np.sum(array))

# Print mean of each row
print("\nMean of each row:")
print(np.mean(array, axis=1))

# Print maximum value in each column
print("\nMax value in each column:")
print(np.max(array, axis=0))