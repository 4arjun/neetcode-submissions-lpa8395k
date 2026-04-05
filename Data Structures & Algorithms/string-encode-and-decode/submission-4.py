class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word)) + '#' + word 
        return encoded

    def decode(self, s: str) -> List[str]:
        strs2 = []
        pt = 0

        while pt<len(s):
            j = pt
            while s[j]!= "#":
                j+=1
            length = int(s[pt:j])
            pt = j+1
            new_s = s[pt:pt+length]
            pt+=length
            strs2.append(new_s)
        return strs2
        
        

