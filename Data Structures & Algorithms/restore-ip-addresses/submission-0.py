class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        def helper(ind, temp):
            if len(temp) == 4:
                if ind == len(s):
                    result.append('.'.join(temp))
                return
            
            for i in range(ind, ind+3):
                if i>=len(s):
                    break
                part = s[ind:i+1]
                if len(part)>1 and part[0] == '0':
                    continue
                if int(part)>255:
                    continue
                temp.append(part)
                helper(i+1, temp)
                temp.pop()
        helper(0, [])
        return result