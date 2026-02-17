"""Write a Python class to get all possible unique subsets from a set of distinct
integers Input:[4,5,6]
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]"""
class Subsets:
    def get_subsets(self, nums):
        result = [[]]
        for n in nums:
            result += [sorted(m + [n]) for m in result]
        return result

input_str=input("Enter the numbers: ")

nums = [int(i) for i in input_str.split(' ')]
obj = Subsets()
print(obj.get_subsets(nums))