# 125. Valid Palindrome
# Solved
# Easy
# Topics
# Companies
# A phrase is a palindrome if, after converting all uppercase letters into lowercase 
# letters and removing all non-alphanumeric characters, it reads the same forward and 
# backward. Alphanumeric characters include letters and numbers.
# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
# Example 3:

# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
# Constraints:
# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

#Solution:

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        
        newString=[]
        # print(s)
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                newString.append(s[i])
        n=len(newString)
        for i in range(n//2):
            if (newString[i]==newString[n-i-1]):
                continue
            else:
                return False
        return True
               
            


