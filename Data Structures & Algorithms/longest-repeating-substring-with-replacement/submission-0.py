class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #so you need to find a continuous set of letters , so as long as k > 2 , keep switching same letters basically
        maxc=0
        cnts = {}
        l=0
        for r in range(len(s)):
            cnts[s[r]]=cnts.get(s[r],0)+1
            maxf=max(cnts.values())
            if (r-l+1)-maxf >k:
                cnts[s[l]]-=1
                l+=1
            maxc = max(maxc,r-l+1)
        return maxc