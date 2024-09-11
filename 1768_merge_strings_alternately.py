class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = str()
        i = 0
        j = 0

        while len(word1) > i and len(word2) > j:
            new_word += word1[i] + word2[j]
            i+=1
            j+=1
        if len(word1) > i:
            new_word += word1[i:]
        elif len(word2) > j:
            new_word += word2[j:]

        return new_word
