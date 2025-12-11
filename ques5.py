def findMaxAverage(nums, k):
    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_avg = window_sum / k
    
    # Slide the window
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i - k] + nums[i]
        max_avg = max(max_avg, window_sum / k)
    
    return max_avg
