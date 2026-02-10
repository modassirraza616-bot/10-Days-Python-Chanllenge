# Given an array arr[]. Your task is to find the minimum and maximum elements
# in the array.
# Examples:
# Input: arr[] = [1, 4, 3, 5, 8, 6]
# Output: [1, 8]
# Explanation: minimum and maximum elements of array are 1 and 8.

# Method1
def getMinMax(arr):
    minimum = arr[0]
    maximum = arr[0]

    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num

    return [minimum, maximum]

# Example
arr = [1, 4, 3, 5, 8, 6]
print(getMinMax(arr))


# Method2
def getMinMax(arr):
    return [min(arr), max(arr)]

arr = [1, 4, 3, 5, 8, 6]
print(getMinMax(arr))
