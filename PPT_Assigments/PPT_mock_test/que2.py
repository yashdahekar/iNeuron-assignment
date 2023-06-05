"""
First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
a. 1 <= s.length <= 10^5
b. s consists of only lowercase English letters.
"""
def firstunique(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for i in range(len(s)):
        if char_count[s[i]] == 1:
            return i

    return -1

s1 = "leetcode"
print(firstunique(s1))  

s2 = "loveleetcode"
print(firstunique(s2))  

s3 = "aabb"
print(firstunique(s3))  

