class Solution:
    def findMin(self, nums: List[int]) -> int:
#         [3,4,5,6,1,2]
#         r = 0 , left = len(nums) , midpoint=left+right //2
#  left < mid < right .-> this case smallest element is first element
#         but there are a few situations for rotated nums : 
#         if left < mid < right then its ordered and left is the answer
#         if left<mid but left > right then search right
#         if left>mid and left is  < right then search right
        l=0
        r=len(nums)-1
        while l<r:
            mid = (r+l)//2
            if nums[mid]>nums[r]:
                l=mid+1
            elif nums[mid]<nums[r]:
                r=mid
        return nums[l]

            