class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l,r = 0, len(nums)-1
        result = [0]*len(nums)
        i=len(nums)-1
        while l<=r:
            if pow(nums[l],2) > pow(nums[r],2):
                result[i]=pow(nums[l],2)
                l+=1
            else:
                result[i]=pow(nums[r],2)
                r-=1
            i-=1

        print(result)
        return result