class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # take a stack and put highest temperature till then ka index in the stack , sooooo , pop the top index and put the index -top index and then update top index 
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]< temperatures[i]:
                node = stack.pop()
                result[node] = i-node
            
            stack.append(i)
        return result