class Solution:
    def groupAnagrams(self, strs: List[str]):
        # we need a dictionary of lists
        dict={}

        for word in strs:
            sortedS="".join(sorted(word)) # we sort the word
            if sortedS not in dict:
                dict[sortedS]=[]
            
            dict[sortedS].append(word)        

        return list(dict.values())