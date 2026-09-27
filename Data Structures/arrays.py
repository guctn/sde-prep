# Array is a collection of items stored at contiguous memory locations. 

arr = [9, 8, 7]
print(arr)          # -> [9, 8, 7]

# Apeend - Insert element at end of array - On average: O(1) amortized
arr.append(6)
print(arr)          # -> [9, 8, 7, 6]

# Pop - Deleting an element at end of array - 0(1)
arr.pop()
print(arr)          # -> [9, 8, 7]

# Insert (not at end of array) - O(n) bc needs to shift the array
arr.insert(2, 5)
print(arr)          # -> [9, 8, 5, 7]

# Delete (not at end of array) - O(n) bc needs to shift the array
arr.pop(-2)
print(arr)          # -> [9, 8, 7]

# Modify an element - O(1) bc we know the exact index
arr[0] = 2
print(arr)          # -> [2, 8, 7]

# Accessing element given index i - O(1)
print(arr[2])       # -> 7

# Checking if array has a specific element - O(n) bc needs to search through the entire array
if 7 in arr:
    print(True)
else:
    print(False)    # -> True

# Checking the size of the array - O(1) bc python stores the lenght
size = len(arr)
print(size)         # -> 3