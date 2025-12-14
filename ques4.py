


def remove_duplicates(arr):
    """
    Remove duplicates from sorted array using two pointers.
    """
    if not arr:
        return 0
    
    # First pointer for unique elements
    unique_idx = 0
    
    # Second pointer to repeat through array
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_idx]:
            unique_idx += 1
            arr[unique_idx] = arr[i]
    
    return unique_idx + 1


def remove_duplicates_value_only(arr):
    """
    Remove duplicates and return only unique values.
    """
    if not arr:
        return arr
    
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            result.append(arr[i])
    
    return result


def remove_duplicates_with_k(arr, k):
   
    if not arr:
        return 0
    
    unique_idx = 0
    count = 1
    
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            count = 1
        
        if count <= k:
            unique_idx += 1
            arr[unique_idx] = arr[i]
    
    return unique_idx + 1


# Test cases
if __name__ == "__main__":
    # Test case 1: Array with duplicates
    test1 = [1, 1, 2, 2, 2, 3, 4, 4, 5]
    print(f"Original array: {test1}")
    arr1 = test1.copy()
    count1 = remove_duplicates(arr1)
    print(f"After removing duplicates: {arr1[:count1]}")
    print(f"Number of unique elements: {count1}")
    print()
    
    # Test case 2: Array without duplicates
    test2 = [1, 2, 3, 4, 5]
    print(f"Original array: {test2}")
    arr2 = test2.copy()
    count2 = remove_duplicates(arr2)
    print(f"After removing duplicates: {arr2[:count2]}")
    print(f"Number of unique elements: {count2}")
    print()
    
    # Test case 3: Array with consecutive duplicates
    test3 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 3]
    print(f"Original array: {test3}")
    arr3 = test3.copy()
    count3 = remove_duplicates(arr3)
    print(f"After removing duplicates: {arr3[:count3]}")
    print(f"Number of unique elements: {count3}")
    print()
    
    # Test case 4: Using value_only version
    test4 = [1, 1, 1, 2, 2, 3, 3, 3, 3, 4]
    print(f"Original array: {test4}")
    result4 = remove_duplicates_value_only(test4)
    print(f"Unique values: {result4}")
    print()
    
    # Test case 5: Allow at most 2 occurrences
    test5 = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    print(f"Original array: {test5}")
    arr5 = test5.copy()
    count5 = remove_duplicates_with_k(arr5, 2)
    print(f"After allowing at most 2 duplicates: {arr5[:count5]}")
    print(f"Number of elements: {count5}")
