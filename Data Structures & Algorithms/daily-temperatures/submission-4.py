class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            stack = []
            result = [0]*len(temperatures)
            for i in range(len(temperatures)):
                if not stack:
                    stack.append(i)
                else: 
                    topindex = stack[-1]
                    while stack and temperatures[stack[-1]]<temperatures[i]:
                        topindex = stack.pop()
                        result[topindex] = i-topindex
                    stack.append(i)
            return result
                    
                