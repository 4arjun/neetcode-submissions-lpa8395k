class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        char_map = {}
        for i in range(len(s)):
            char_map[s[i]] = i
        max_reachable = 0
        print(char_map)
        start = 0
        end = 0
        result = []
        while start<len(s):
            max_reachable = max(max_reachable, char_map[s[end]])
            while end<=max_reachable:
                max_reachable = max(max_reachable, char_map[s[end]])
                end+=1
                print(max_reachable)
            result.append(end-start)
            start = end
        return result

            
