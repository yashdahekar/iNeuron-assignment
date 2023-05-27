"""Q1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output0 [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Solution: """

print("question 1 output ==> ")

def twosum(nums, target):
    # Create a dictionary to store the complement of each number
    complement_dict = {}

    # Iterate through the array
    for i, num in enumerate(nums):
        # Check if the complement exists in the dictionary
        if num in complement_dict:
            # If found, return the indices of the current number and its complement
            return [complement_dict[num], i]
        else:
            # If not found, add the current number's complement to the dictionary
            complement = target - num
            complement_dict[complement] = i

    # If no solution is found, return an empty list
    return []

nums = [2, 7, 11, 15]
target = 9
result = twosum(nums, target)
print(result)


"""
💡 **Q2.** Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
- Return k.

**Example :**
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_*,_*]

**Explanation:** Your function should return k = 2, with the first two elements of nums being 2. It does not matter what you leave beyond the returned k (hence they are underscores)

Solution: """

print("question 2 output ==> ")

def removeElement(nums, val):
    # Initialize a pointer to keep track of the position where non-val elements should be placed
    k = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is not equal to val, move it to the position indicated by the pointer
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    # Return the number of elements that are not equal to val
    return k

nums = [3, 2, 2, 3]
val = 3
result = removeElement(nums, val)
print("Output:", result)
print("Modified nums:", nums[:result])


"""
Q3.Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5

Output: 2
 """


print("question 3 output ==> ")

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # At this point, the target value was not found in the array
    # The variable 'left' represents the index where the target would be inserted
    return left

nums = [1, 3, 5, 6]
target = 5
result = searchInsert(nums, target)
print("Output:", result)


"""
💡Q4. You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.

Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].


"""

print("question 4 output ==> ")

def plusOne(digits):
    n = len(digits)

    # Iterate through the digits in reverse order
    for i in range(n - 1, -1, -1):
        # If the current digit is less than 9, we can simply increment it and return the updated array
        if digits[i] < 9:
            digits[i] += 1
            return digits

        # If the current digit is 9, we set it to 0 and propagate the carry operation
        digits[i] = 0

    # If we reach this point, it means all digits were 9, so we need to add an additional digit 1 at the beginning
    return [1] + digits


digits = [1, 2, 3]
result = plusOne(digits)
print("Output:", result)


""" 
💡 **Q5.** You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

**Example 1:**
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]

**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

"""

print("question 5 output ==> ")

def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1, nums2, and the merged array
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1

    # Iterate from the end of both arrays
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] <= nums2[p2]:
            # If the element in nums1 is smaller or equal, place it in the merged array
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            # If the element in nums2 is smaller, place it in the merged array
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    # If there are remaining elements in nums2, place them in the merged array
    nums1[:p2 + 1] = nums2[:p2 + 1]


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print("Output:", nums1)



'''Q6. Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]

Output: true '''

print("question 6 output ==> ")

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)

    return False

nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print("Output:", result)



""" **Q7.** Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

Note that you must do this in-place without making a copy of the array.

**Example 1:**
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0] """

print("question 7 output ==> ")

def moveZeroes(nums):
    # Initialize two pointers: one to track the position to place the next nonzero element,
    # and another to iterate through the array.
    next_nonzero = 0

    # Iterate through the array
    for i in range(len(nums)):
        # If the current element is nonzero, move it to the position indicated by the next_nonzero pointer
        if nums[i] != 0:
            nums[next_nonzero] = nums[i]
            next_nonzero += 1

    # After moving all nonzero elements, fill the remaining positions with zeros
    while next_nonzero < len(nums):
        nums[next_nonzero] = 0
        next_nonzero += 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print("Output:", nums)


""" **Q8.** You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

**Example 1:**
Input: nums = [1,2,2,4]
Output: [2,3]"""

print("question 8 output ==> ")

def findErrorNums(nums):
    n = len(nums)

    # XOR all the numbers from 1 to n
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i

    # XOR all the elements in nums
    xor_nums = 0
    for num in nums:
        xor_nums ^= num

    # XOR the result with xor_all to obtain the XOR of the duplicate number and the missing number
    xor_result = xor_all ^ xor_nums

    # Find the rightmost set bit in xor_result
    rightmost_set_bit = xor_result & ~(xor_result - 1)

    # Partition the elements in nums and 1 to n based on the rightmost set bit
    xor_dup = 0
    xor_missing = 0
    for num in nums:
        if num & rightmost_set_bit:
            xor_dup ^= num
        else:
            xor_missing ^= num

    for i in range(1, n + 1):
        if i & rightmost_set_bit:
            xor_dup ^= i
        else:
            xor_missing ^= i

    # Check which number is missing by comparing with nums
    for num in nums:
        if num == xor_dup:
            return [xor_dup, xor_missing]

    # If no duplicate is found, it means xor_dup is the missing number
    return [xor_missing, xor_dup]


nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print("Output:", result)
