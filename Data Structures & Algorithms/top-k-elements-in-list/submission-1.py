class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i]+=1
            else:
                dict1[i]=1
        sorted_dict = dict(
    sorted(dict1.items(), key=lambda item: item[1], reverse=True)
)
        
        j =0
        result = []
        for key in sorted_dict.keys():
            if j < k: 
                result.append(key)
                j+=1
            else:
                break
        return result
            
        