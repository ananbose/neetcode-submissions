class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1= {}
        for ind, i in enumerate(nums):

            if target-i in dict1:
                return [dict1[target-i], ind]
            dict1[i]=ind
        
