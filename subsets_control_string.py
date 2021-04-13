set = "abcd"  # the set
N = len(set) # size
subsets = [""]

while set:
    cand = set[0]
    set=set[1:]

    no_subsets = [k for k in subsets]
    yes_subsets = [k + cand for k in subsets]
    subsets = no_subsets + yes_subsets

print(f"{'subsets: ':14}{str(subsets)}")
print(f"{'len(subsets): ':14}{str(len(subsets))}")
print(f"{'2**N: ':14}{2**N}")
