def numone(nums):
    # assume nums is sorted and contains only 0, 1s
    start = 0
    final = len(nums) - 1
    mid = (final + start) // 2
    if len(nums) == 0:
        return 0
    if nums[start] == 1:  # all ones
        return len(nums)
    if nums[final] == 0:  # all zeros
        return 0

    # Definition: The Special Zero is a 0 followed by a 1
    # Assertion: There is a single "Special Zero" in nums (given conditions enforced above)
    # Loop Invariant: the Special Zero is in [start, final)
    while final > start:
        if nums[mid] == 0:
            if nums[mid + 1] == 1:
                # nums[mid] is the Special Zero, enforce the loop invariant
                start = mid
                final = mid
            else:  # nums[mid+1] == 0
                # the Special Zero occurs at mid+1 or greater
                start = mid + 1
                final = final
        else:  # nums[mid] == 1
            # the Special Zero occurs before mid
            start = start
            final = mid
        mid = (final + start) // 2

    num_zeros = start + 1
    return len(nums) - num_zeros


assert numone([]) == 0
assert numone([0]) == 0
assert numone([0, 0]) == 0
assert numone([0, 0, 0]) == 0

assert numone([1]) == 1
assert numone([0, 1]) == 1
assert numone([0, 0, 1]) == 1
assert numone([0, 0, 0, 1]) == 1

assert numone([1, 1]) == 2
assert numone([0, 1, 1]) == 2
assert numone([0, 0, 1, 1]) == 2
assert numone([0, 0, 0, 1, 1]) == 2
