class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=collections.defaultdict(list)
        for s in strs:
            # word=s
             
            sortedS=''.join(sorted(s)) # simply sorted(s) gives the characters pf s in alpha order.
            dict[sortedS].append(s)

        return list(dict.values())