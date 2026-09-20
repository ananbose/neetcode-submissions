class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0 or len(s)==1:
            return len(s)
        start=0
        sub = s[start]
        maxl=1
        seen = {s[start]:start}

        for i in range(start+1,len(s)):
            if s[i] not in sub:
                sub = sub+s[i]
                maxl = max(len(sub), maxl)
                seen[s[i]]=i
            else:
                index = seen[s[i]]   
                if index+1 < len(s):
                  sub=s[index+1:i+1]
                  seen[s[i]]=i

        return maxl
