'''Given two strings ransomNote and magazine, return true if ransomNote 
can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        counter = 0

        for i in ransomNote:
            if i in dict:
                dict.update({ i : dict[i]+1})
            else:
                dict.update({ i : 1})

        for key, value in dict.items():
            for char in magazine:
                if char == key:
                    counter+=1
                if value == counter:
                    break
            if value != counter:
                return False
            counter = 0
        return True

# Runtime: 7ms
# Memory: 18MB