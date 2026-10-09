class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        for u, v, w in times:
            graph.setdefault(u, []).append((v, w))
        heap = []
        visited = set()
        heapq.heappush(heap,(0,k))
        while heap:
            dist, node  = heapq.heappop(heap)
            if node in visited :
                continue
            visited.add(node)
            if len(visited)==n:
                return dist
            for neighbor, d in graph.get(node,[]):
                if neighbor not in visited:
                    heapq.heappush(heap,(dist+d, neighbor))
        return -1


