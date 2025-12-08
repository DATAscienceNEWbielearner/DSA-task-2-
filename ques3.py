

def find_missing_number(nums):
   
    n = len(nums) + 1  # Since one number is missing
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


def find_missing_number_xor(nums):
   
    n = len(nums) + 1
    result = 0
    
    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        result ^= i
    
    # XOR with all array elements
    for num in nums:
        result ^= num
    
    return result


def find_missing_number_set(nums):
   
    n = len(nums) + 1
    expected_set = set(range(1, n + 1))
    actual_set = set(nums)
    return (expected_set - actual_set).pop()


# Test cases
if __name__ == "__main__":
    # Test case 1: Numbers 1-5, missing 3
    test1 = [1, 2, 4, 5]
    print(f"Array: {test1}")
    print(f"Missing number (Math): {find_missing_number(test1)}")
    print(f"Missing number (XOR): {find_missing_number_xor(test1)}")
    print(f"Missing number (Set): {find_missing_number_set(test1)}")
    print()
    
    # Test case 2: Numbers 1-10, missing 7
    test2 = [1, 2, 3, 4, 5, 6, 8, 9, 10]
    print(f"Array: {test2}")
    print(f"Missing number (Math): {find_missing_number(test2)}")
    print(f"Missing number (XOR): {find_missing_number_xor(test2)}")
    print(f"Missing number (Set): {find_missing_number_set(test2)}")
    print()
    
    # Test case 3: Numbers 1-3, missing 1
    test3 = [2, 3]
    print(f"Array: {test3}")
    print(f"Missing number (Math): {find_missing_number(test3)}")
    print(f"Missing number (XOR): {find_missing_number_xor(test3)}")
    print(f"Missing number (Set): {find_missing_number_set(test3)}")
