class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums)==0:
            return 0
        nums.sort()

        start=0
        maxl,l =1,1
        for i in range(start,len(nums)-1):
            if nums[i+1]==nums[i]:
                continue
            elif nums[i]+1==nums[i+1]:
                l+=1
                maxl=max(maxl,l)
            else:
                start=i
                l=1
        return maxl
        
