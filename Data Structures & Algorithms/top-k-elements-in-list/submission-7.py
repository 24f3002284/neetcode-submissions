class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={} # to store the freq of each chrctr

        for i,n in enumerate(nums):
            dict[n]=dict.get(n,0)+1

        listOfLists=collections.defaultdict(list) # max possible freq of a chrctr in a list=len of that list
        for ch in dict:
            listOfLists[dict[ch]].append(ch)

        ans=[]

        for i in range(len(nums),-1,-1):
            if k>0:
                if(len(listOfLists[i])!=0):
                    ans.extend(listOfLists[i])
                    k-=len(listOfLists[i])

        return ans
