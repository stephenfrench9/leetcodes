N = 18  # size of the set

subsets = [""]
num_elements_considered = 0

while num_elements_considered < N:
    num_elements_considered += 1
    no_subsets = [k + "n" for k in subsets]
    yes_subsets = [k + "y" for k in subsets]
    subsets = no_subsets + yes_subsets

print(f"{'subsets: ':14}{str(subsets)}")
print(f"{'len(subsets): ':14}{str(len(subsets))}")
print(f"{'2**N: ':14}{2**N}")
