class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result =[]
        intervals.sort()
        result =[intervals[0]]
        for i in range(1,len(intervals)):
            before = result[-1]
            after = intervals[i]
            if before[1]<after[0]:
                result.append(after)
            else:
                result[-1] = [before[0],max(before[1], after[1])]
        return result
                    