# https://stackoverflow.com/questions/11868964/list-comprehension-returning-two-or-more-items-for-each-item

from functools import reduce

f    = lambda x: f"f({x})" ## Just for example
g    = lambda x: f"g({x})"
data = [1, 2, 3]


def whats(acc, x):
    return acc + [f(x), g(x)]

reduce(whats, data, [])


# oh this sounds kind of nice.
# you have something that you are accumulating, and you call your function on what you have accumulated so far and each element sequentially.
# The first element is the accumulation, and the second element to your reduction function is an element in the list.
