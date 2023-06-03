"""Given an integer array nums of length n and an integer target, find three integers
in nums such that the sum is closest to the target.
Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2

Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
give python solution 
"""
print("Que no. 1")


def threeSumClosest(nums, target):
    nums.sort()  # Sort the array in ascending order
    closest_sum = float('inf')  # Initialize the closest sum to infinity

    for i in range(len(nums) - 2):
        left = i + 1  # Pointer for the element to the right of nums[i]
        right = len(nums) - 1  # Pointer for the last element in the array

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                return current_sum  # Exact match, return the sum

            # Update the closest sum if the current sum is closer to the target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum < target:
                left += 1  # Move the left pointer to increase the sum
            else:
                right -= 1  # Move the right pointer to decrease the sum

    return closest_sum


# Example usage
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)


"""Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:
           ● 0 <= a, b, c, d < n
           ● a, b, c, and d are distinct.
           ● nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]"""

print("Que no. 2")
def fourSum(nums, target):
    nums.sort()  # Sort the array in ascending order
    n = len(nums)
    quadruplets = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate values for the first element

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue  # Skip duplicate values for the second element

            left = j + 1  # Pointer for the element to the right of nums[j]
            right = n - 1  # Pointer for the last element in the array

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    quadruplets.append([nums[i], nums[j], nums[left], nums[right]])

                    # Skip duplicate values for the third and fourth elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1  # Move the left pointer to increase the sum
                else:
                    right -= 1  # Move the right pointer to decrease the sum

    return quadruplets


# Example usage
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(result)


""" A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
[1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater
permutation of its integer. More formally, if all the permutations of the array are
sorted in one container according to their lexicographical order, then the next
permutation of that array is the permutation that follows it in the sorted container.

If such an arrangement is not possible, the array must be rearranged as the
lowest possible order (i.e., sorted in ascending order).

● For example, the next permutation of arr = [1,2,3] is [1,3,2].
● Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
● While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
have a lexicographical larger rearrangement.

Given an array of integers nums, find the next permutation of nums.
The replacement must be in place and use only constant extra memory.

**Example 1:**
Input: nums = [1,2,3]
Output: [1,3,2]"""

print("Que no. 3")
def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Find the first pair of adjacent elements where nums[i] < nums[i+1]
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1

        # Find the smallest element in nums[i:] that is greater than nums[i-1]
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        # Swap nums[i-1] with nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the subarray nums[i:]
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# Example usage
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)


"""Given a sorted array of distinct integers and a target value, return the index if the
target is found. If not, return the index where it would be if it were inserted in
order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2"""

print("Que no. 4")
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

    # If the target is not found, return the index where it would be inserted
    return left


# Example usage
nums = [1, 3, 5, 6]
target = 5
index = searchInsert(nums, target)
print(index)

"""You are given a large integer represented as an integer array digits, where each
digits[i] is the ith digit of the integer. The digits are ordered from most significant
to least significant in left-to-right order. The large integer does not contain any
leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
Input: digits = [1,2,3]
Output: [1,2,4]

**Explanation:** The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

"""
print("Que no. 5")
def plusOne(digits):
    n = len(digits)

    for i in range(n - 1, -1, -1):
        if digits[i] != 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    # If there is still a carry-over left after iterating through all digits
    digits.insert(0, 1)
    return digits


# Example usage
digits = [1, 2, 3]
result = plusOne(digits)
print(result)

"""Given a non-empty array of integers nums, every element appears twice except
for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only
constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1"""

print("Que no. 6")
def singleNumber(nums):
    result = 0

    for num in nums:
        result ^= num

    return result


# Example usage
nums = [2, 2, 1]
result = singleNumber(nums)
print(result)

"""You are given an inclusive range [lower, upper] and a sorted unique integer array
nums, where all elements are within the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in
nums.

Return the shortest sorted list of ranges that exactly covers all the missing
numbers. That is, no element of nums is included in any of the ranges, and each
missing number is covered by one of the ranges.

Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: [[2,2],[4,49],[51,74],[76,99]]

Explanation: The ranges are:
[2,2]
[4,49]
[51,74]
[76,99]"""

print("Que no. 7")
def findMissingRanges(nums, lower, upper):
    missingRanges = []

    # Helper function to add missing range to the result
    def addRange(start, end):
        if start == end:
            missingRanges.append(str(start))
        else:
            missingRanges.append(str(start) + '->' + str(end))

    # Check for missing numbers before the first element
    if nums[0] > lower:
        addRange(lower, nums[0] - 1)

    # Check for missing numbers between consecutive elements
    for i in range(len(nums) - 1):
        if nums[i + 1] != nums[i] + 1:
            addRange(nums[i] + 1, nums[i + 1] - 1)

    # Check for missing numbers after the last element
    if nums[-1] < upper:
        addRange(nums[-1] + 1, upper)

    return missingRanges


# Example usage
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)

"""Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false
"""
print("Que no. 8")

def canAttendMeetings(intervals):
    # Sort the intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    # Check for overlapping intervals
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False

    return True


# Example usage
intervals = [[0, 30], [5, 10], [15, 20]]
result = canAttendMeetings(intervals)
print(result)
