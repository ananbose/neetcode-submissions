class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ''
        res = s[0]
        for i in range(len(s)):
            r = i+1
            l = i-1
            while l>=0 and r<len(s) and s[r]==s[l] :
                lw=r-l+1
                if len(res)<lw:
                    res=s[l:r+1]
                r+=1
                l-=1 
            #Nextevn
            l=i
            r=i+1
            while  l>=0 and r<len(s) and s[r]==s[l]:
                lw=r-l+1
                if len(res)<lw:
                    res=s[l:r+1]
                r+=1
                l-=1 
        return res

