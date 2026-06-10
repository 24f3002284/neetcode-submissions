class Solution:
    def groupAnagrams(self, strs: List[str]):
        # we need a dictionary of lists
        dict=collections.defaultdict(list)

        for word in strs:
            sortedS="".join(sorted(word)) # we sort the word
            dict[sortedS].append(word)        

        return list(dict.values())