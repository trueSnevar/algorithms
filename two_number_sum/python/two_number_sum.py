"""
  Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
  If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order.
  If no two numbers sum up to the target sum, the function should return an empty array.
  Assume that there will be at most one pair of numbers summing up to the target sum.

  > Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
  < Sample output: [-1, 11]
"""


# Solution 1; O(n^2) time | O(1) space:
# least effective one -> two for loops

def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        first_num = array[i]
        for j in range(i + 1, len(array)):
            second_num = array[j]
            if first_num + second_num == targetSum:
                return sorted([first_num, second_num])
    return []

print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
