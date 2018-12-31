"""
  Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
  If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order.
  If no two numbers sum up to the target sum, the function should return an empty array.
  Assume that there will be at most one pair of numbers summing up to the target sum.

  > Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
  < Sample output: [-1, 11]
"""

# Solution 2; O(nlog(n)) time | O(1) space:
# sorting input array first

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
