class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        m = {}
        for word in strs:
            chars = [0] * 26
            for char in word:
                chars[ord(char) - 97] += 1
            if tuple(chars) not in m:
                m[tuple(chars)] = []
            m[tuple(chars)].append(word)
        return list(m.values())