class Solution:
    def isPalindrome(self, s: str) -> bool:

        news=''
        for i in s:
            i= i.lower()
            if i.isalnum():
                news=news+i
        newsl = list(news)
        last = len(newsl)-1
        first = 0

        while first<=last:
            if newsl[first]== news[last]:
                first+=1
                last-=1
                continue
            else:
                return False
        return True

            
            
                
        