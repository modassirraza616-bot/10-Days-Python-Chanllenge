# You are given an array of integers arr[]. You have to reverse the given array.
# Note: Modify the array in place.
# Examples:
# Input: arr = [1, 4, 3, 2, 6, 5]
# Output: [5, 6, 2, 3, 4, 1]


#Method 1
def reverseArray(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = [1, 4, 3, 2, 6, 5]
reverseArray(arr)
print(arr)


# Method 2
arr = [1, 4, 3, 2, 6, 5]
arr.reverse()
print(arr)
