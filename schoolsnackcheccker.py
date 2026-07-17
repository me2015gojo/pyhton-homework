fruits = {"apple", "banana", "mango"}
print(fruits)

fruits.add("orange")
print(fruits)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
common = set1.intersection(set2)
print(common)

import array
nums = array.array('i', [10, 20, 30])
print(nums)

nums.insert(1, 15)
nums.append(40)
print(nums)

print(nums.count(20))
nums.reverse()
print(nums)