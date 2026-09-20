class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # nums[i] + nums[j] + nums[k]=0
        # nums[i] = -( nums[j]+ nums[k])
        # -nums[i]=nums[j]+nums[k]
        result = []
        nums.sort()
        for i in range(len(nums)):
            target = - nums[i]
            if i>0 and nums[i] == nums[i-1]:
                continue
            #if i+1<len(nums)-1:
            l=i+1
            r=len(nums)-1
            while l<r:
                if nums[l]+nums[r]>target:
                    r=r-1
                elif nums[l] + nums[r] == target:
                    result.append([nums[i], nums[l], nums[r]])
                    r=r-1
                    l=l+1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

                elif nums[l]+nums[r]<target:
                    l=l+1
        return result

                     
            