class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left+=1
                right-=1
            return True
        left = 0 
        right = len(s)-1
        while left < right:
            if s[left]==s[right]:
                left+=1
                right-=1
                continue
            elif isPalindrome(left+1,right) and left+1 < len(s)  or (isPalindrome(left, right-1) and right-1>=0) :
                return True
            else:
                return False
        return True