# map(func, *iterables) 
# With map() functions, it's not only easier, but it's also much more flexible.
# zip() function is a function that takes a number of iterables and then creates a tuple containing each of the elements in the iterables.


# filter(func, iterable)
# filter(), first of all, requires the function to return boolean values (true or false) and then passes each element in the iterable through the function, 
# "filtering" away those that are false
# A "palindrome" is a word, phrase, or sequence that reads the same backwards as forwards.

# reduce(func, iterable[, initial])
# reduce applies a function of two arguments cumulatively to the elements of an iterable, optionally starting with an initial argument

# Exercise
# In this exercise, you'll use each of map, filter, and reduce to fix broken code. 

from functools import reduce 

# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than 
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: round(x**2, 3), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)