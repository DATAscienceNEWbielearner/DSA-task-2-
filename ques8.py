def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]
    
    # Phase 1: Detect cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Phase 2: Find cycle start (the duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow


# Alternative: Using Set (simpler approach)
def findDuplicateSet(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1


# Test cases
if __name__ == "__main__":
    # Test 1 - Floyd's cycle detection
    nums1 = [1, 3, 4, 2, 2]
    print(findDuplicate(nums1))  # Output: 2
    
    # Test 2
    nums2 = [3, 1, 3, 4, 2]
    print(findDuplicate(nums2))  # Output: 3
    
    # Test 3 - Using set approach
    nums3 = [1, 4, 4, 2, 4]
    print(findDuplicateSet(nums3))  # Output: 4
