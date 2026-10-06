class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        tot = nums[0]
        maxTotal = tot
        for i in range(1,len(nums)):
            curr = nums[i]
            tot = max(curr , curr+tot)
            maxTotal = max(tot, maxTotal)
        return maxTotal