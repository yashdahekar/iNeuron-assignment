print("que no 1. ==>")

def minimumDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + ord(s1[i - 1])
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + ord(s2[j - 1])
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))
    return dp[m][n]
s1 = "sea"
s2 = "eat"
result = minimumDeleteSum(s1, s2)
print(result) 

print("que no 2. ==>")

def isValid(s):
    stack = []

    for c in s:
        if c in '(*':
            stack.append(c)
        elif c == ')':
            if not stack:
                return False
            while stack and stack[-1] != '(':
                stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()

    while stack and stack[-1] == '*':
        stack.pop()

    return len(stack) == 0

s = "()"
result = isValid(s)
print(result)  

print("que no 3. ==>")

def minSteps(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[m][n]

word1 = "sea"
word2 = "eat"
result = minSteps(word1, word2)
print(result)  

print("que no 4. ==>")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructTree(s, start, end):
    if start > end:
        return None

    splitIndex = -1
    openCount = 0

    for i in range(start, end + 1):
        if s[i] == '(':
            openCount += 1
        elif s[i] == ')':
            openCount -= 1

        if openCount == 0:
            splitIndex = i
            break

    nodeValue = int(s[start:splitIndex])
    node = TreeNode(nodeValue)

    node.left = constructTree(s, splitIndex + 1, s.index(')', splitIndex))
    node.right = constructTree(s, s.index('(', splitIndex + 1) + 1, end - 1)

    return node

def preorderTraversal(root):
    if root is None:
        return []

    result = [root.val]
    result += preorderTraversal(root.left)
    result += preorderTraversal(root.right)

    return result

s = "4(2(3)(1))(6(5))"
root = constructTree(s, 0, len(s) - 1)
result = preorderTraversal(root)
print(result) 


print("que no 5. ==>")

def compress(chars):
    write_index = 0
    count = 1

    for i in range(1, len(chars) + 1):
        if i < len(chars) and chars[i] == chars[i - 1]:
            count += 1
        else:
            chars[write_index] = chars[i - 1]
            write_index += 1

            if count > 1:
                count_str = str(count)
                for j in range(len(count_str)):
                    chars[write_index] = count_str[j]
                    write_index += 1

            count = 1

    return write_index

chars = ["a","a","b","b","c","c","c"]
new_length = compress(chars)
print(new_length) 
print(chars[:new_length])  

print("que no 6. ==>")

def findAnagrams(s, p):
    result = []
    p_freq = {}
    window_freq = {}

    for char in p:
        p_freq[char] = p_freq.get(char, 0) + 1

    left, right = 0, 0
    window_size = len(p)

    while right < len(s):
        window_freq[s[right]] = window_freq.get(s[right], 0) + 1

        if right - left + 1 == window_size:
            if p_freq == window_freq:
                result.append(left)

            window_freq[s[left]] -= 1
            if window_freq[s[left]] == 0:
                del window_freq[s[left]]
            left += 1

        right += 1

    return result

s = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)  

print("que no 7. ==>")

def decodeString(s):
    stack = []
    for ch in s:
        if ch == ']':
            sub_string = ''
            while stack[-1] != '[':
                sub_string = stack.pop() + sub_string
            stack.pop() 
            k = ''
            while stack and stack[-1].isdigit():
                k = stack.pop() + k
            k = int(k)
            
            stack.append(sub_string * k)
        else:
            stack.append(ch)
    
    return ''.join(stack)

s = "3[a]2[bc]"
result = decodeString(s)
print(result)  

print("que no 8. ==>")

def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        return len(set(s)) < len(s)

    mismatches = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            mismatches.append(i)

    if len(mismatches) != 2:
        return False

    i, j = mismatches
    return s[i] == goal[j] and s[j] == goal[i]

s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)  
