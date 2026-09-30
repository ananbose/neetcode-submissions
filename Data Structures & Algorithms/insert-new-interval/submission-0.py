class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        result.append(newInterval)
        for interval in intervals:
            i,j = interval
            #if the current interval is overlapping with new interval take min of both as i and max of both as j
            #1,3 and 2,5. 1,2 2,3 1,6 and 
            p,q = result.pop()
                
            if j<p:
                result.append([i,j])
                result.append([p,q])
                
            elif i>q:
                result.append([p,q])
                result.append([i,j])
            else:
                result.append([min(i,p), max(j,q)])
        return result

