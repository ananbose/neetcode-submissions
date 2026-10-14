class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if stack and stack[-1][0] == i and stack[-1][1]+1 == k:
                stack.pop()
            elif stack and stack[-1][0] == i:
                stack[-1][1]+=1
            else:
                stack.append([i,1])
        print(stack)
        result= ''
        for letter,count in stack:
            while count>0:
                result+=letter
                count-=1
        return result
