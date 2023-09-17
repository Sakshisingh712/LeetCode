# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

#Solution:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n=len(strs)
        strs.sort()
        output=''
        a=strs[0]
        b=strs[n-1]
        for i in range(len(strs[0])):
            if a[i]==b[i]:
                output+=a[i]
            else:
                break; 
        # print(output)
        return output
        
            

