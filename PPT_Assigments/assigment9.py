print("que no 1. ==>")
def isPowerOfTwo(n):
    if n <= 0:
        return False
    return n & (n - 1) == 0

n = 1
result = isPowerOfTwo(n)
print(result)  

n = 16
result = isPowerOfTwo(n)
print(result)  

n = 3
result = isPowerOfTwo(n)
print(result)  

print("que no 2. ==>")

sum = (n * (n + 1)) / 2
def sumOfFirstNNumbers(n):
    sum = (n * (n + 1)) // 2
    return sum
n = 3
result = sumOfFirstNNumbers(n)
print(result)  
n = 5
result = sumOfFirstNNumbers(n)
print(result)  


print("que no 3. ==>")

def factorial(N):
    fact = 1
    for i in range(1, N + 1):
        fact *= i
    return fact
N = 5
result = factorial(N)
print(result)  
N = 4
result = factorial(N)
print(result)  

print("que no 4. ==>")
def calculateExponent(N, P):
    result = N ** P
    return result
N = 5
P = 2
result = calculateExponent(N, P)
print(result)  
N = 2
P = 5
result = calculateExponent(N, P)
print(result)  

print("que no 5. ==>")

def findMax(arr, index):
    if index == len(arr) - 1:
        return arr[index]
    
    current = arr[index]
    subarray_max = findMax(arr, index + 1)
    
    return max(current, subarray_max)

arr = [1, 4, 3, -5, -4, 8, 6]
result = findMax(arr, 0)
print(result)  

arr = [1, 4, 45, 6, 10, -8]
result = findMax(arr, 0)
print(result) 

print("que no 6. ==>")

def findNthTerm(a, d, N):
    NthTerm = a + (N - 1) * d
    return NthTerm

a = 2
d = 1
N = 5
result = findNthTerm(a, d, N)
print(result)  

a = 5
d = 2
N = 10
result = findNthTerm(a, d, N)
print(result)  


print("que no 7. ==>")

def permute(s, l, r):
    if l == r:
        print(''.join(s))
    else:
        for i in range(l, r + 1):
            s[l], s[i] = s[i], s[l] 
            permute(s, l + 1, r)   
            s[l], s[i] = s[i], s[l]  

def generatePermutations(S):
    n = len(S)
    s = list(S)
    permute(s, 0, n - 1)
    
S = "ABC"
generatePermutations(S)

S = "XY"
generatePermutations(S)

print("que no 8. ==>")

def findProduct(arr):
    product = 1
    for num in arr:
        product *= num
    return product

arr = [1, 2, 3, 4, 5]
result = findProduct(arr)
print(result) 

arr = [1, 6, 3]
result = findProduct(arr)
print(result)  
