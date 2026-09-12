class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        for st in s:
            if st not in dict1:
                dict1[st]=1
            else:
                dict1[st]+=1
        for tt in t:
            if tt not in dict1:
                return False
            else:
                dict1[tt]-=1
        for d in dict1.values():
            if d!=0:
                return False
        return True