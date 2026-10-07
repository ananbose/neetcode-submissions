class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        l = len(strs[0])
        res =''
        for i in range(l):
            for j in range(len(strs)-1):
                if strs[j][i]==strs[j+1][i]:
                    continue
                else:
                    return res
            res = strs[0][0:i+1]
        return res
            
