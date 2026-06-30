class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += str(len(word))+"#"+word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i <len(s):
            j = i
            while s[j]!= "#":
                j+=1
            length = int(s[i:j])
            j+=1
            word = s[j:j+length]
            decoded_strs.append(word)
            i = j+length

        return decoded_strs

        
