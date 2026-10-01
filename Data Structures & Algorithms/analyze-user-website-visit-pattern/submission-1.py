from itertools import combinations
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        graph = {}
        for ind , i in enumerate(username):
            if i in graph:
                graph[i].append((website[ind], timestamp[ind]))
            else:
                graph[i]=[(website[ind],timestamp[ind])]
        for user in graph:
            graph[user].sort(key=lambda x: x[1])
        graphfreq = {}
        for user in graph:
            listwebsites=[]
            for website, ts in graph[user]:
                listwebsites.append(website)
            combs = (set(combinations(listwebsites,3)))
            print("hello",combs)
            for comb in combs:
                if comb in graphfreq:
                    graphfreq[comb]+=1
                else:
                    graphfreq[comb]=1
        print(graphfreq)
        maxfreq = max(graphfreq.values())

        candidates = []

        for pattern in graphfreq:
            if graphfreq[pattern] == maxfreq:
                candidates.append(pattern)

        return list(min(candidates))    