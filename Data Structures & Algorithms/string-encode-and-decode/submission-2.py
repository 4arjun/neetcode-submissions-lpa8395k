class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s+=word
            s+="["
        return s


    def decode(self, s: str) -> List[str]:
        result = []
        st = ""
        for char in s:
            if char!="[":
                st+=char    
            else:
                result.append(st)
                st = ""
        return result


        