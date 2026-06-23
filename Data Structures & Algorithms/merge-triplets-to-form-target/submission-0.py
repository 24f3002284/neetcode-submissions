class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good=set()
        tarF,tarS,tarT=target[0],target[1],target[2]

        for f,s,t in triplets:
            if f>tarF or s>tarS or t>tarT:
                continue
            if f==tarF:
                good.add(0)#tarF is reachable by this triplet
            if s==tarS:
                good.add(1)
            if t==tarT:
                good.add(2)

        return len(good)==3