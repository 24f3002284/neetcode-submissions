class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq=defaultdict(int)
        for n in hand:
            freq[n]+=1

        hand.sort()
        i=0
        for card in hand:
            if freq[card]==0:
                continue

            for j in range(card,card+groupSize):
                if freq[j]==0:
                    return False

                freq[j]-=1#DF!!

        return True

