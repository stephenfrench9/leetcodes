set1 = [1,2,3,4,5]
expected_num_subsets = 2**len(set1)

# initialize valid state, the only subset is the empty set.
considered_set = []
subsets = [[]]

for e in set1:
    considered_set.append(e) # break state
    new_sets = []
    for subset in subsets:
        new_set = subset.copy()
        new_set.append(e)
        new_sets.append(new_set)

    subsets = subsets + new_sets


print(len(subsets))
print(expected_num_subsets)

# There is probably a functional way to do this, with a double list comprehension, or functools.reduce
# what is better, a = a + b, or a.append(b) for b in b]
