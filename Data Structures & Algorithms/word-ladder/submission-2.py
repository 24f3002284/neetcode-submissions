class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj=collections.defaultdict(list)
        if endWord not in wordList:
            return 0

        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                adj[pattern].append(word)

        q=deque([beginWord])
        visited=set()
        visited.add(beginWord)
        res=1
        while q:
            for _ in range(len(q)):
                node=q.popleft()
                
                if node==endWord:
                    return res

                for i in range(len(node)):
                    pattern=node[:i]+"*"+node[i+1:]
                    for nei in adj[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

            res+=1
        return 0