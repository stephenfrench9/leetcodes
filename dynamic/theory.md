

# Dynamic Programming

## House Robber

The trivial solution is to build every possible path through the array (every possible subsequence) and then compute the total cost for each subsequence, and then choose the highest cost. It is obvious that you will find the best path because you literally considered all of them.

A path starts at -2 or -1, and increments by 2 or 3 each time. 

#### Naive Solution

```
best = 0
pathes = [[-2], [-1]]
while pathes:
    for path in pathes:
        # grow the path
        # if the path is off the end, drop it from the array and compare its cost to 'best'. 
```

#### Dynamic Programming Solution

When you do this, you see that many of the paths (subsequences) go through the same index in the array. These paths will be identical for the remainder of the traversal, and so you can trim the paths you are looking at by choosing the better path for a given index.

To put this into practice, you can traverse the index, at each point saving only the best path for that index. In this way, you have eliminated extraneous branches found in the naive solution.

**only add a given element to a single path, the best path so far**

```
for n in num:
    # look back a few spaces, and see which of the paths that can reach this element is the biggest
```

Are there only two paths? I think so ...

You could trim out inferior and repeated paths in different ways too. One way is to build all the paths, but record the best discovered so far per index, and drop paths that arrive at that index with an inferior score. If they beat the previous, then you might be out of luck, the previous might already be in the queue. 

