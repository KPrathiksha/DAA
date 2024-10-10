def rob(nums):
    def rob_line(nums):
        prev, curr = 0, 0
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr

    n = len(nums)
    if n == 1:  
        return nums[0]
    case1 = rob_line(nums[:-1])
    case2 = rob_line(nums[1:])
    
    return max(case1, case2)

nums = [2, 3, 2]
print(rob(nums))  # Output: 3
