class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        suf = []
        for i in range(0,len(nums)):
            if i-1<0:
                pre.append(1)
            else:
                pre.append(pre[i-1]*nums[i-1])

        result = []
        suf = [1]*len(nums)
        for i in range(len(nums)-2,-1,-1):
                suf[i]=nums[i+1]*suf[i+1]

        for i in range(0,len(nums)):
            result.append(pre[i]*suf[i])
        return result
