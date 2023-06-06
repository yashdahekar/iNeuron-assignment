print("Que no. 1 == >") 

def reconstruct_permutation(s):
    perm = []
    n = len(s)
    low, high = 0, n

    for c in s:
        if c == 'I':
            perm.append(low)
            low += 1
        elif c == 'D':
            perm.append(high)
            high -= 1

    perm.append(low)  # Append the last remaining integer

    return perm

reconstruct_permutation("IDID") 

print("Que no. 2 == >") 

def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n

        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)

print("Que no. 3 == >") 

def validMountainArray(arr):
    n = len(arr)
    
    if n < 3:
        return False
    
    left = 0
    right = n - 1
    
    while left < right:
        if arr[left] < arr[left + 1]:
            left += 1
        elif arr[right] < arr[right - 1]:
            right -= 1
        else:
            break
    
    return left == right and left != 0 and right != n - 1

arr = [2, 1]
print(validMountainArray(arr))

print("Que no. 4 == >") 

def findMaxLength(nums):
    max_length = 0
    count = 0
    sum_dict = {0: -1}  # Initialize with a sum of 0 at index -1

    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count == 0:
            max_length = i + 1
        elif count in sum_dict:
            max_length = max(max_length, i - sum_dict[count])
        else:
            sum_dict[count] = i

    return max_length
nums = [0, 1]
print(findMaxLength(nums))

print("Que no. 5 == >") 
def minProductSum(nums1, nums2):
    n = len(nums1)
    nums1.sort()
    nums2.sort()
    min_product_sum = 0

    for i in range(n):
        min_product_sum += nums1[i] * nums2[n - 1 - i]

    return min_product_sum
nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
print(minProductSum(nums1, nums2))

print("Que no. 6 == >") 

from collections import defaultdict

def findOriginalArray(changed):
    count_dict = defaultdict(int)

    for num in changed:
        count_dict[num] += 1

    original = []

    for num in changed:
        if num % 2 == 0 and count_dict[num] > 0:
            count_dict[num] -= 1

            if count_dict[num] == 0:
                del count_dict[num]

            original.append(num // 2)
        else:
            return []

    return original

changed = [1, 3, 4, 2, 6, 8]
print(findOriginalArray(changed))

print("Que no. 7 == >") 

def generateMatrix(n):
    result = [[0] * n for _ in range(n)]
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1
    num = 1

    while row_start <= row_end and col_start <= col_end:
        
        for j in range(col_start, col_end + 1):
            result[row_start][j] = num
            num += 1
        row_start += 1

        for i in range(row_start, row_end + 1):
            result[i][col_end] = num
            num += 1
        col_end -= 1

        if row_start <= row_end:
            for j in range(col_end, col_start - 1, -1):
                result[row_end][j] = num
                num += 1
            row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                result[i][col_start] = num
                num += 1
            col_start += 1

    return result

n = 3
result = generateMatrix(n)
print(result)


print("Que no. 8 == >") 

def multiply(mat1, mat2):
    m = len(mat1)
    k = len(mat2)
    n = len(mat2[0])
    
    result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for p in range(k):
                result[i][j] += mat1[i][p] * mat2[p][j]

    return result

mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
result = multiply(mat1, mat2)
print(result)
