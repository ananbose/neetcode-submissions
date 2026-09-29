class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isP(sub):
            mid = (len(sub))//2

            if len(sub)%2==0 :
                left = sub[:mid]
                right = sub[mid:]
                if left == right[::-1]:
                    return True
            elif len(sub)%2!=0:
                left = sub[:mid]
                right = sub[mid+1:]
                if left == right[::-1]:
                    return True
            return False
                
        if isP(s):
            return True        
        l=0
        r=len(s)-1
        k =1
        while l<=r:
            if s[r]==s[l]:
                r-=1
                l+=1
            else:
                if(l+1<=r and isP(s[:l]+s[l+1:])):
                    return True
                if (r-1 >l and isP(s[0:r]+s[r+1:])):
                    return True
                else:
                    return False
