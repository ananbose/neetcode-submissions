class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #choose the number
            #check if the sum is reached and then add it to the result list
            #if sum is less than target then choose the number again
            #also choose the next number
        #dont choose the number
            #choose the next number
        result = []
        def dfs(i,res):
            if i == len(nums):
                return
            #ake it??
            if nums[i]+sum(res)<=target:
                res.append(nums[i])
                if sum(res) == target:
                    result.append(res.copy())
                else:
                    dfs(i,res)
                res.pop()
            dfs(i+1,res)
            
            
        dfs(0,[])
        return result