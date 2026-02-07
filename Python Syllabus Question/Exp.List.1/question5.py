# Given an array arr[]. The task is to find the largest element and return it.
# Examples:
# Input: arr[] = [1, 8, 7, 56, 90]
# Output: 90
# Explanation: The largest element of the given array is 90

# Method1
arr = [1, 8, 7, 56, 90]

largest = arr[0]
for num in arr:
    if num > largest:
        largest = num

print(largest)

# Method2
arr = [1, 8, 7, 56, 90]
print(max(arr))
