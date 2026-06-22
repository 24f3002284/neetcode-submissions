class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n=len(words)
        adjL={ch:[] for word in words for ch in word}

        #filling adjL
        for i in range(n-1):
            w1,w2=words[i],words[i+1]
            minLen=min(len(w1),len(w2))

            if len(w1)>len(w2) and w1[:minLen]==w2[:minLen]:#doesnot satisfy reqd condn
                return ""

            for j in range(minLen):
                if w1[j]!=w2[j]:
                    adjL[w1[j]].append(w2[j])
                    break#imp!! add only first chrctr of difference to the grph

        cycle=set()
        visited=set()
        res=[]
        def dfs(ch):
            if ch in cycle:
                return False
            if ch in visited:
                return True

            cycle.add(ch)
            for descedant in adjL[ch]:
                if not dfs(descedant):
                    return False#false, immediately after finding out a cycle or a loop

            cycle.remove(ch)
            visited.add(ch)
            res.append(ch)#append chrctrs after fully visiting them and their descedants
            #the node without any descedants willbe added first into res
            return True

        for ch in adjL:
            if not dfs(ch):
                return ""
        
        res.reverse()
        return "".join(res)

        