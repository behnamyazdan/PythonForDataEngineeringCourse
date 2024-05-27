# Array Manipulation in NumPy

Array manipulation in NumPy involves various operations for reshaping, stacking, and splitting arrays. These operations are essential for transforming and organizing data efficiently.

## Reshaping Arrays

Reshaping arrays involves changing the shape or dimensions of an array without changing the data it contains. This is useful for tasks such as converting between different dimensionalities or preparing data for specific operations.

**1. Reshaping Arrays**

```python
import numpy as np

# Create a 1D array
arr_1d = np.arange(12)

# Reshape to a 2D array
arr_2d = arr_1d.reshape(3, 4)

print("Original 1D array:")
print(arr_1d)
print("\nReshaped 2D array:")
print(arr_2d)
```

Output:
```
Original 1D array:
[ 0  1  2  3  4  5  6  7  8  9 10 11]

Reshaped 2D array:
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

**2. Reshaping with -1**

```python
# Reshape with -1 to infer the size automatically
arr_2d_auto = arr_1d.reshape(2, -1)

print("Auto-reshaped 2D array:")
print(arr_2d_auto)
```

Output:
```
Auto-reshaped 2D array:
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]]
```

## Stacking Arrays

Stacking arrays involves combining multiple arrays along a specified axis to create a new array. This is useful for concatenating data from different sources or combining arrays for further processing.

**1. Horizontal Stacking**

```python
# Create two arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Horizontal stacking
stacked_horizontal = np.hstack((arr1, arr2))

print("Horizontal stacked array:")
print(stacked_horizontal)
```

Output:
```
Horizontal stacked array:
[[1 2 5 6]
 [3 4 7 8]]
```

**2. Vertical Stacking**

```python
# Vertical stacking
stacked_vertical = np.vstack((arr1, arr2))

print("Vertical stacked array:")
print(stacked_vertical)
```

Output:
```
Vertical stacked array:
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
```

## Splitting Arrays

Splitting arrays involves dividing a single array into multiple smaller arrays along a specified axis. This is useful for partitioning data for parallel processing or organizing data into more manageable chunks.

**1. Horizontal Splitting**

```python
# Create an array
arr = np.arange(12).reshape(3, 4)

# Horizontal splitting
split_horizontal = np.hsplit(arr, 2)

print("Horizontal split arrays:")
for arr_split in split_horizontal:
    print(arr_split)
```

Output:
```
Horizontal split arrays:
[[0 1]
 [4 5]
 [8 9]]
[[ 2  3]
 [ 6  7]
 [10 11]]
```

**2. Vertical Splitting**

```python
# Vertical splitting
split_vertical = np.vsplit(arr, 3)

print("Vertical split arrays:")
for arr_split in split_vertical:
    print(arr_split)
```

Output:
```
Vertical split arrays:
[[0 1 2 3]]
[[4 5 6 7]]
[[ 8  9 10 11]]
```

---

These operations are fundamental for organizing and transforming data efficiently in numerical computing tasks.