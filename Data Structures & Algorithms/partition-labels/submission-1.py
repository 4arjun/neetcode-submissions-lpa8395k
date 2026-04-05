class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_map = {}
        for i in range(len(s)):
            char_map[s[i]] = i
        result = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, char_map[s[i]])
            if i == end:
                result.append(end-start+1)
                start=i+1
        return result