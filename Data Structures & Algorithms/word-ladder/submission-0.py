class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        #find all the words that have one letter off and then for that word find all the words with one letter off , keep doing that till you get the right word , if you dont return 0
        q = deque()
        q.append([beginWord,1])
        words = set(wordList)
        letters = "abcdefghijklmnopqrstuvwxyz"
        while q:
            node, dist = q.popleft()
            if node == endWord:
                return dist
            for i in range(len(node)):
                for c in letters:
                    if node[:i]+c+node[i+1:] in words:
                        words.remove(node[:i]+c+node[i+1:] )
                        q.append([node[:i]+c+node[i+1:], dist+1])
        return 0
        