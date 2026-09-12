class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num]=1
            else:
                return True
        return False
    
        