print("Que no. 1 ==> ")

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        
        if s_char in s_to_t:
            if s_to_t[s_char] != t_char:
                return False
        else:
            s_to_t[s_char] = t_char
        
        if t_char in t_to_s:
            if t_to_s[t_char] != s_char:
                return False
        else:
            t_to_s[t_char] = s_char
    
    return True

s = "egg"
t = "add"
print(isIsomorphic(s, t))  # Output: True

print("Que no. 2 ==> ")

def isStrobogrammatic(num):
    strobogrammatic_dict = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    left, right = 0, len(num) - 1
    
    while left <= right:
        if num[left] not in strobogrammatic_dict or strobogrammatic_dict[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    
    return True

num = "69"
print(isStrobogrammatic(num))  # Output: True

print("Que no. 3 ==> ")

def addStrings(num1, num2):
    result = ""
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    
    while i >= 0 or j >= 0 or carry > 0:
        x = int(num1[i]) if i >= 0 else 0
        y = int(num2[j]) if j >= 0 else 0
        
        digit_sum = x + y + carry
        carry = digit_sum // 10
        digit = digit_sum % 10
        
        result = str(digit) + result
        i -= 1
        j -= 1
    
    return result

num1 = "11"
num2 = "123"
print(addStrings(num1, num2))  # Output: "134"

print("Que no. 4 ==> ")

def reverse_words(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence

s = "Let's take LeetCode contest"
reversed_sentence = reverse_words(s)
print(reversed_sentence)


print("Que no. 5 ==> ")
def reverse_str(s, k):
    chars = list(s)

    for i in range(0, len(chars), 2 * k):
        chars[i:i+k] = chars[i:i+k][::-1]

    reversed_str = ''.join(chars)

    return reversed_str

s = "abcdefg"
k = 2
reversed_str = reverse_str(s, k)
print(reversed_str)

print("Que no. 6 ==> ")
def can_shift(s, goal):
    s = s + s
    if goal in s:
        return True
    else:
        return False
s = "abcde"
goal = "cdeab"
result = can_shift(s, goal)
print(result)

print("Que no. 7 ==> ")
def process_string(string):
    stack = []
    for char in string:
        if char == '#':
            if stack:
                stack.pop()
        else:
            stack.append(char)
    return ''.join(stack)

def backspace_compare(s, t):
    processed_s = process_string(s)
    processed_t = process_string(t)
    return processed_s == processed_t

s = "ab#c"
t = "ad#c"
result = backspace_compare(s, t)
print(result)

print("Que no. 8 ==> ")
def checkStraightLine(coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    reference_slope = (y2 - y1) / (x2 - x1)
    
    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        slope = (y - y1) / (x - x1)
        if slope != reference_slope:
            return False
    
    return True
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(checkStraightLine(coordinates))
