"""Given three integer arrays arr1, arr2 and arr3 **sorted** in **strictly increasing** order,
 return a sorted array of **only** the integers that appeared in **all** three arrays.

**Example 1:**

Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]

Output: [1,5]

**Explanation:** Only 1 and 5 appeared in the three arrays."""

print("Que no. 1 ==> ")

def findCommonElements(arr1, arr2, arr3):
    ptr1 = ptr2 = ptr3 = 0
    result = []

    while ptr1 < len(arr1) and ptr2 < len(arr2) and ptr3 < len(arr3):
        if arr1[ptr1] == arr2[ptr2] == arr3[ptr3]:
            result.append(arr1[ptr1])
            ptr1 += 1
            ptr2 += 1
            ptr3 += 1
        elif arr1[ptr1] < arr2[ptr2] or arr1[ptr1] < arr3[ptr3]:
            ptr1 += 1
        elif arr2[ptr2] < arr1[ptr1] or arr2[ptr2] < arr3[ptr3]:
            ptr2 += 1
        elif arr3[ptr3] < arr1[ptr1] or arr3[ptr3] < arr2[ptr2]:
            ptr3 += 1

    return result

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

result = findCommonElements(arr1, arr2, arr3)
print(result)

"""# Given two **0-indexed** integer arrays nums1 and nums2, return *a list* answer *of size* 2 *where:*
# - answer[0] *is a list of all **distinct** integers in* nums1 *which are **not** present in* nums2*.*
# - answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.
# **Note** that the integers in the lists may be returned in **any** order.
# **Example 1:**
# **Input:** nums1 = [1,2,3], nums2 = [2,4,6]
# **Output:** [[1,3],[4,6]]
# **Explanation:**
# For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
# For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6]."""
print("Que no. 2 ==> ")

def findDistinctElements(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    result1 = [num for num in set1 if num not in set2]
    result2 = [num for num in set2 if num not in set1]
    return [result1, result2]

nums1 = [1,2,3]
nums2 = [2,4,6]

result = findDistinctElements(nums1, nums2)
print(result)


"""💡 Given a 2D integer array matrix, return *the **transpose** of* matrix.
The **transpose** of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
**Example 1:**
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
"""
print("Que no. 3 ==> ")

def transposeMatrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result

matrix = [[1,2,3],[4,5,6],[7,8,9]]

result = transposeMatrix(matrix)
print(result)


""" Given an integer array nums of 2n integers,
 group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is **maximized**. Return *the maximized sum*.
**Example 1:**
Input: nums = [1,4,3,2]
Output: 4
**Explanation:** All possible pairings (ignoring the ordering of elements) are:
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
So the maximum possible sum is 4"""
print("Que no. 4 ==> ")

def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum

nums = [1, 4, 3, 2]

result = arrayPairSum(nums)
print(result)

"""You have n coins and you want to build a staircase with these coins.
 The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase **may be** incomplete.
Given the integer n, return *the number of **complete rows** of the staircase you will build*.
**Example 1:**
Explanation:** Because the 3rd row is incomplete, we return 2."""

print("Que no. 5 ==> ")
def arrangeCoins(n):
    left = 0
    right = n

    while left <= right:
        mid = left + (right - left) // 2
        curr = (mid * (mid + 1)) // 2

        if curr == n:
            return mid

        if curr < n:
            left = mid + 1
        else:
            right = mid - 1

    return right

n = 5

result = arrangeCoins(n)
print(result)

"""Given an integer array nums sorted in **non-decreasing** order, return *an array of **the squares of each number** sorted in non-decreasing order*.
**Example 1:**
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
**Explanation:** After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]"""
print("Que no. 6 ==> ")

def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    left = 0
    right = n - 1
    index = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] * nums[left]
            left += 1
        else:
            result[index] = nums[right] * nums[right]
            right -= 1
        index -= 1

    return result

nums = [-4, -1, 0, 3, 10]

result = sortedSquares(nums)
print(result)

"""
You are given an m x n matrix M initialized with all 0
's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
Count and return *the number of maximum integers in the matrix after performing all the operations*
**Example 1:**
**Input:** m = 3, n = 3, ops = [[2,2],[3,3]]
**Output:** 4
**Explanation:** The maximum integer in M is 2, and there are four of it in M. So return 4."""
print("Que no. 7 ==> ")

def maxCount(m, n, ops):
    min_row = m
    min_col = n

    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])

    return min_row * min_col

m = 3
n = 3
ops = [[2, 2], [3, 3]]

result = maxCount(m, n, ops)
print(result)

"""Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
*Return the array in the form* [x1,y1,x2,y2,...,xn,yn].
**Example 1:**
**Input:** nums = [2,5,1,3,4,7], n = 3
**Output:** [2,3,5,4,1,7]
**Explanation:** Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7]."""
print("Que no. 8 ==> ")

def shuffle(nums, n):
    result = []
    i = 0
    j = n

    while i < n:
        result.append(nums[i])
        result.append(nums[j])
        i += 1
        j += 1

    return result

nums = [2, 5, 1, 3, 4, 7]
n = 3

result = shuffle(nums, n)
print(result)
