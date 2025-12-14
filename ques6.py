def sortColors(nums):
    left = 0
    right = len(nums) - 1
    mid = 0
    
    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
        else:
            mid += 1
    
    return nums


# Test cases
if __name__ == "__main__":
    # Test 1
    nums1 = [2, 0, 2, 1, 1, 0]
    sortColors(nums1)
    print(nums1)  # Output: [0, 0, 1, 1, 2, 2]
    
    # Test 2
    nums2 = [2, 0, 1]
    sortColors(nums2)
    print(nums2)  # Output: [0, 1, 2]
    
    # Test 3
    nums3 = [0]
    sortColors(nums3)
    print(nums3)  # Output: [0]
