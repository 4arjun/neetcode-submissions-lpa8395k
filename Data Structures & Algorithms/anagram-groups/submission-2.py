class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagrams = defaultdict(list)
        for word in strs:
            unicode = [0]*26
            for char in word:
                unicode[ord(char)-97]+=1
            anagrams[tuple(unicode)].append(word)
        return list(anagrams.values())
            


        