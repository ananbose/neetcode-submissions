class Solution:
    def isValid(self, s: str) -> bool:
        #keep a dictionary of brackets and put brackets into a stack , for every cloing bracket , you take out the upper most bracket if it matches , if it doesnt then return false and if there is any opening bucket left in the stack then also return False
        dict1 = {')':'(', '}':'{',']':'['}
        stack = []
        for i in s :
            if i in dict1.values():
                stack.append(i)
            else:
                if len(stack) > 0 and stack[-1] == dict1[i]:
                    stack.pop()
                else:
                    return False
        return True if len(stack) == 0 else False
