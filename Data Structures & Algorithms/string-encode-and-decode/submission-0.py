class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            encoded += str(len(word)) + '#' + word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        while s:
            seperator_idx = s.index('#')
            length = int(s[:seperator_idx])
            word_idx = len(str(length)) + 1
            word = s[word_idx:word_idx+length]
            s = s[word_idx+length:]
            decoded.append(word)
        return decoded