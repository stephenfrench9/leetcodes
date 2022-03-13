nums = [1, 2, 3, 3, 5, 7, 9, 3, 11, 0, 14, 16, 12, 13]
stack = [-float('inf')]

for e in nums:
    if e >= stack[-1]:
        stack.append(e)
    else:
        while e < stack[-1]:
            stack.pop()
        stack.append(e)


