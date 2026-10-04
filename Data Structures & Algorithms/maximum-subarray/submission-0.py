class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        maxlen = nums[0]
        for i in range(1,len(nums)):
            curr = max(nums[i],curr+nums[i])
            maxlen = max(maxlen, curr)
        return maxlen
        