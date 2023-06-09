print("Que no. 1 ==> ")
def mySqrt(x):
    if x <= 1:
        return x

    left = 0
    right = x

    while left <= right:
        mid = (left + right) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

    return right
print(mySqrt(4))

print("Que no. 2 ==> ")
def findPeakElement(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left
nums = [1, 2, 3, 1]
print(findPeakElement(nums))

print("Que no. 3 ==> ")
def missingNumber(nums):
    n = len(nums)
    missing = n

    for i in range(n):
        missing ^= i ^ nums[i]

    missing ^= n

    return missing
nums = [3, 0, 1]
print(missingNumber(nums))

print("Que no. 4 ==> ")

def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
nums = [1, 3, 4, 2, 2]
print(findDuplicate(nums))

print("Que no. 5 ==> ")
def intersection(nums1, nums2):
    set1 = set(nums1)
    intersection = []

    for num in nums2:
        if num in set1:
            intersection.append(num)
            set1.remove(num)

    return intersection
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))

print("Que no. 6 ==> ")
def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
nums = [3, 4, 5, 1, 2]
print(findMin(nums))

print("Que no. 7 ==> ")
def searchRange(nums, target):
    def findLeft(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def findRight(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    left = findLeft(nums, target)
    right = findRight(nums, target)

    if left <= right:
        return [left, right]
    else:
        return [-1, -1]
nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))

print("Que no. 8 ==> ")
def intersect(nums1, nums2):
    freqMap = {}
    for num in nums1:
        freqMap[num] = freqMap.get(num, 0) + 1

    intersection = []
    for num in nums2:
        if num in freqMap and freqMap[num] > 0:
            intersection.append(num)
            freqMap[num] -= 1

    return intersection
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))
