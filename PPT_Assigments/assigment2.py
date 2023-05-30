""""
Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., 
(an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
 """
print("Que number 1")

def arrayPairSum(nums):
    nums.sort()  # Sort the array in ascending order
    max_sum = 0
    
    for i in range(0, len(nums), 2):
        max_sum += nums[i]  # Sum the minimum value of each pair
    
    return max_sum

nums = [1, 4, 3, 2]
print(arrayPairSum(nums))  ## output 4 

"""
Alice has n candies, where the ith candy is of type candyType[i]. 
Alice noticed that she started to gain weight, so she visited a doctor. 
The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). 
Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while 
still following the doctor's advice. 
Given the integer array candyType of length n, return the maximum number of different types of candies she can
 eat if she only eats n / 2 of them.
"""
print("Que number 2")

def distributeCandies(candyType):
    # Calculate the maximum number of candies Alice can eat (n/2)
    max_candies = len(candyType) // 2
    
    # Count the number of unique candy types
    unique_candies = len(set(candyType))
    
    # Return the minimum of the maximum candies and unique candies
    return min(max_candies, unique_candies)

candyType = [1, 1, 2, 2, 3, 3]
print(distributeCandies(candyType)) ## output 3 


"""
We define a harmonious array as an array where the difference between its maximum value
and its minimum value is exactly 1.
Given an integer array nums, return the length of its longest harmonious subsequence
among all its possible subsequences.
A subsequence of an array is a sequence that can be derived from the array by deleting 
some or no elements without changing the order of the remaining elements.
"""
print("Que number 3")

from collections import Counter

def findLHS(nums):
    counter = Counter(nums)  # Count the frequency of each number
    
    max_length = 0
    
    for num in counter:
        if num + 1 in counter:
            length = counter[num] + counter[num + 1]
            max_length = max(max_length, length)
    
    return max_length

nums = [1, 3, 2, 2, 5, 2, 3, 7]
print(findLHS(nums)) ## output 5 

"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers
rule and false otherwise.
"""
print("Que number 4")

def canPlaceFlowers(flowerbed, n):
    count = 0
    i = 0
    
    while i < len(flowerbed):
        if (
            flowerbed[i] == 0 and 
            (i == 0 or flowerbed[i - 1] == 0) and 
            (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
        ):
            flowerbed[i] = 1  # Plant a flower
            count += 1
            i += 2  # Skip the next plot since it cannot have a flower
        else:
            i += 1
    
    return count >= n

flowerbed = [1, 0, 0, 0, 1]
n = 1
print(canPlaceFlowers(flowerbed, n)) ## output True

"""
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.
"""
print("Que number 5")

def maximumProduct(nums):
    nums.sort()  # Sort the array in ascending order
    
    # Calculate the product of the three largest numbers
    max_product = nums[-1] * nums[-2] * nums[-3]
    
    # Calculate the product of the two smallest numbers and the largest number
    min_product = nums[0] * nums[1] * nums[-1]
    
    # Return the maximum product between the two calculated products
    return max(max_product, min_product)

nums = [1, 2, 3]
print(maximumProduct(nums)) ## output 6

"""
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise,
return -1.

You must write an algorithm with O(log n) runtime complexity."""
print("Que number 6")

def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        
        if target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target)) ## output 4 

"""
An array is monotonic if it is either monotone increasing or monotone decreasing.
An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
monotone decreasing if for all i <= j, nums[i] >= nums[j].
Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""
print("Que number 7")

def isMonotonic(nums):
    increasing = decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False
        if nums[i] > nums[i - 1]:
            decreasing = False
    
    return increasing or decreasing

nums = [1, 2, 2, 3]
print(isMonotonic(nums)) ## output True

"""
You are given an integer array nums and an integer k.
In one operation, you can choose any index i where 0 <= i < nums.length and
change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. You can apply this operation at most once for each index i.
The score of nums is the difference between the maximum and minimum elements in nums.
Return the minimum score of nums after applying the mentioned operation at most once for each index in it.
"""

print("Que number 8")
def minimumScore(nums, k):
    nums.sort()  # Sort the array in ascending order
    
    # Calculate the difference between the maximum and minimum elements
    score = nums[-1] - nums[0]
    
    # Iterate through the array except for the first and last elements
    for i in range(1, len(nums) - 1):
        # Calculate the potential minimum and maximum values after applying the operation
        potential_min = nums[i] - k
        potential_max = nums[i] + k
        
        # Update the score by considering the potential minimum and maximum values
        score = min(score, max(nums[-1], potential_min) - min(nums[0], potential_max))
    
    return score

nums = [1]
k = 0
print(minimumScore(nums, k)) ## output 0
