class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
# At nums[i]:

# TAKE it
#     append nums[i]
#     if target reached → save
#     otherwise recurse with SAME i
#     pop

# SKIP it
    #recurse with i + 1
        def getComb(i,res):
            if i==len(nums):
                return
            if sum(res)+nums[i]<=target:
                res.append(nums[i])
                if sum(res)==target:
                    result.append(res.copy())
                else:
                    getComb(i,res)
                res.pop()
            
            getComb(i+1,res)
        
        nums.sort()
        result = []
        
        getComb(0,[])
        return result