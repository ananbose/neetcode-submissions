class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        result.append(newInterval)
        flag = []
        for index , interval in enumerate(intervals):
            i,j = interval
            p,q = result.pop()
            if j<p:
                result.append([i,j])
                result.append([p,q])
                
            elif i>q:
                result.append([p,q])
                flag.append(index)
                break
            else:
                result.append([min(i,p), max(j,q)])
        if (flag):
            index = flag.pop()
            for i in range(index,len(intervals)):
                result.append(intervals[i])
        return result

