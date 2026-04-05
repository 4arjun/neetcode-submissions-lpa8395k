class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map_anagram = defaultdict(list)
        for st in strs:
            unicode = [0]*26
            for char in st:
                unicode[ord(char)-ord('a')] += 1
            map_anagram[str(unicode)].append(st)
        result = []
        for key, val in map_anagram.items():
            result.append(val)
        return result

