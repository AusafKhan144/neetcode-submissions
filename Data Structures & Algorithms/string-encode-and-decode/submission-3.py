class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        delimiter = '#'
        for s in strs:
            word_length = len(s)
            encoded += f"{word_length}{delimiter}{s}"


        return encoded



    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        delimiter = '#'
        
        while i < len(s):
            j = i
            while s[j] != delimiter:
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded.append(s[i:j])
            i = j
        
        return decoded

            


        
