def moveNegativeToLeft(nums):
    # Two pointer approach
    left = 0
    right = len(nums) - 1
    
    while left < right:
        # Move left pointer until we find a positive number
        while left < right and nums[left] < 0:
            left += 1
        
        # Move right pointer until we find a negative number
        while left < right and nums[right] >= 0:
            right -= 1
        
        # Swap if left < right
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    return nums


# Test cases
if __name__ == "__main__":
    # Test 1
    nums1 = [1, -2, 3, -4, 5, -6]
    moveNegativeToLeft(nums1)
    print(nums1)  # Output: [-2, -4, -6, 3, 5, 1] or similar (negatives on left)
    
    # Test 2
    nums2 = [-1, -2, 3, 4, 5]
    moveNegativeToLeft(nums2)
    print(nums2)  # Output: [-1, -2, 3, 4, 5]
    
    # Test 3
    nums3 = [5, 4, 3, -2, -1]
    moveNegativeToLeft(nums3)
    print(nums3)  # Output: [-2, -1, 3, 4, 5]
