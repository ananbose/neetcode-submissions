class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r = len(nums)-1
        l = 0
        while (l<=r):
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid]<=nums[r]:
                if nums[mid] < target <= nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        
        return -1
        