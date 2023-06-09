print("que no 1. ==>")

def is_power_of_three(n):
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1
print(is_power_of_three(27))  
print(is_power_of_three(0))   

print("que no 2. ==>")

def last_remaining(n):
    if n == 1:
        return 1

    return 2 * (n // 2 + 1 - last_remaining(n // 2))

print(last_remaining(9)) 

print("que no 3. ==>")

def print_subsets(string, subset='', index=0):
    if index == len(string):
        print(subset)
        return

    print_subsets(string, subset, index + 1)
    print_subsets(string, subset + string[index], index + 1)  
    
string = "abc"
print_subsets(string)

string1 = "abc"
print_subsets(string1)

string2 = "abcd"
print_subsets(string2)

print("que no 4. ==>")

def calculate_length(string):
    if string == "":
        return 0
    else:
        return 1 + calculate_length(string[1:])

string1 = "Hello"
print(calculate_length(string1))  

string2 = "Recursion"
print(calculate_length(string2))  

print("que no 5. ==>")

def count_contiguous_substrings(S):
    count = 0
    for i in range(len(S)):
        count += 1
        for j in range(i + 1, len(S)):
            if S[j] == S[i]:
                count += 1
            else:
                break
    return count

S1 = "abcab"
print(count_contiguous_substrings(S1))  

S2 = "aba"
print(count_contiguous_substrings(S2))  

print("que no 6. ==>")

def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("move disk 1 from rod", source, "to rod", destination)
        return 1

    moves = (
        tower_of_hanoi(n - 1, source, destination, auxiliary) +
        1 +
        tower_of_hanoi(n - 1, auxiliary, source, destination)
    )

    print("move disk", n, "from rod", source, "to rod", destination)

    return moves

N = 2
total_moves = tower_of_hanoi(N, 1, 2, 3)
print(total_moves)


print("que no 7. ==>")

def permute_string(string, left, right):
    if left == right:
        print("".join(string))
    else:
        for i in range(left, right + 1):
            string[left], string[i] = string[i], string[left]
            permute_string(string, left + 1, right)
            string[left], string[i] = string[i], string[left]  
str1 = "cd"
n = len(str1)
permute_string(list(str1), 0, n - 1)

print("que no 8. ==>")

def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in string:
        if char.lower() in consonants:
            count += 1
    return count
string1 = "abc de"
print(count_consonants(string1))  

string2 = "geeksforgeeks portal"
print(count_consonants(string2))  
