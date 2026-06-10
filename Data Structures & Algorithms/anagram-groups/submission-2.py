class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict=collections.defaultdict(list)
        for s in strs:
            # word=s
             
            sortedS=''.join(sorted(s))
            dict[sortedS].append(s)

        return list(dict.values())