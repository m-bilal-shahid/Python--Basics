# Python List Methods 

# append()
# Adds an element at the end of the list
fruits = ["apple", "banana"]
fruits.append("cherry")


# extend()
# Adds multiple items from another list or iterable at the end
a = [1, 2, 3]
b = [4, 5]
a.extend(b)


# insert()
# Inserts an element at a specific index
numbers = [10, 30, 40]
numbers.insert(1, 20)


# remove()
# Removes the first occurrence of a specified value
fruits = ["apple", "banana", "apple"]
fruits.remove("apple")


# pop()
# Removes and returns an element by index
# If index not given, removes the last element
numbers = [10, 20, 30]
numbers.pop(1)


# clear()
# Removes all elements from the list
items = [1, 2, 3]
items.clear()


# index()
# Returns the index of the first occurrence of a value
nums = [10, 20, 30]
nums.index(20)


# count()
# Returns how many times a specific value appears in the list
data = [1, 2, 2, 3, 2]
data.count(2)


# sort()
# Sorts the list in ascending order (default)
# Use reverse=True for descending order
nums = [4, 1, 3, 2]
nums.sort()
nums.sort(reverse=True)


# reverse()
# Reverses the order of the list
nums = [1, 2, 3]
nums.reverse()


# copy()
# Returns a shallow copy of the list
a = [1, 2, 3]
b = a.copy()


# max()
# Returns the largest element of the list
max([2, 5, 1])


# min()
# Returns the smallest element of the list
min([2, 5, 1])


# sum()
# Returns the sum of all numeric elements in the list
sum([1, 2, 3])


# sorted()
# Returns a new sorted copy of the list
nums = [3, 1, 2]
sorted(nums)


# len()
# Returns total number of elements in the list
fruits = ["apple", "banana"]
len(fruits)


# any()
# Returns True if any element of the list is True
any([0, 1, 0])


# all()
# Returns True if all elements of the list are True
all([1, 2, 3])
all([0, 1, 2])


# del
# Deletes a specific index or entire list
nums = [10, 20, 30]
del nums[1]


# reversed()
# Returns a reversed iterator of the list
nums = [1, 2, 3]
for i in reversed(nums):
    pass


# list()
# Converts an iterable (string, tuple, etc.) to a list
chars = list("hello")


# * operator
# Repeats the list multiple times
[1, 2] * 3
