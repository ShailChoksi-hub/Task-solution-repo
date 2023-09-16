# Function 
def find_max_min(arr):
    if len(arr) == 0:
        print("Array is empty")
        return

    maximum = max(arr)
    minimum = min(arr)

    print(f"Maximum is: {maximum}")
    print(f"Minimum is: {minimum}")

# Test arrays
arr1 = [1, 2, 3, 4, 5]
find_max_min(arr1)

arr2 = [5, 3, 7, 4, 2]
find_max_min(arr2)
