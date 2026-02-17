"""Write a Python class to find a pair of elements (indices of the two numbers)
from a given array whose sum equals a specific target number.
Input: numbers= [10,20,10,40,50,60,70], target=50
Output: 3, 4."""
class SumFinder:
    def find_indices(self, numbers, target):
        lookup = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in lookup:
                return lookup[diff], i
            lookup[num] = i

numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50
obj = SumFinder()
print(obj.find_indices(numbers, target))