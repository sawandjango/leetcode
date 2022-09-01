'''
https://leetcode.com/problems/ransom-note/
383. Ransom Note
Easy

2813

355

Add to List

Share
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

## Solution 1 : Take two dictionaires 

from unittest.mock import MagicMixin

'''
class Soulution:
    def canConstruct(self, ransomeNote:str, magazine:str ) -> bool:
        rannote_dic = {}
        mg_dic = {}

        for ran_c in ransomeNote:
            if ran_c not in rannote_dic:
                rannote_dic[ran_c] = 1
            else: 
                rannote_dic[ran_c] +=1    

        for mg_c in magazine:
            if mg_c not in mg_dic:
                mg_dic[mg_c] = 1
            else:
                mg_dic[mg_c] +=1
        for ch in ransomeNote:
            if ch not in mg_dic or mg_dic[ch] < rannote_dic[ch]:
                return False
        return True                    

sol = Soulution()
result = sol.canConstruct("sawan","sawchhn")
print(result)
# Time complexity - O(M+N)
# Space O(M+N)

## Another solution : You can reuce space complexity by using the same dictionary
'''
class Solution2:
    def conConstruct(self, randomeStr:str, magazineStr:str) -> bool:
        magazine_dict = {}
        for c in magazineStr:
            if c not in magazine_dict:
                magazine_dict[c] =1
            else:
                magazine_dict[c] +=1

        for ch in randomeStr:
            if ch not in magazine_dict or magazine_dict[ch] ==0:
                return False
            else:
                magazine_dict[ch] -=1    
        return True
sol = Solution2()
result = sol.conConstruct("aa","ab")
print(result)
