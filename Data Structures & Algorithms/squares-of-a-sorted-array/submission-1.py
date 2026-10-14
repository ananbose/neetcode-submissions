class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        left = 0
        right = len(nums)-1
        i=len(nums)-1
        while left <= right :
            if pow(nums[left],2) > pow(nums[right],2):
                result[i] = pow(nums[left],2)
                i-=1
                left+=1
            else:
                result[i] = pow(nums[right],2)
                i-=1
                right-=1
        return result
