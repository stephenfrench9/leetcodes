# https://leetcode.com/problems/longest-increasing-subsequence/
from typing import List

class Solution:
    # this is logic that I never needed to write.
    @staticmethod
    def is_increasing(new_sub):
        if len(new_sub) == 0 or len(new_sub) == 1:
            return True

        for i in range(len(new_sub))[1:]:
            increase = new_sub[i] > new_sub[i-1]
            if not increase:
                return False

        return True


    def lengthOfLIS(self, nums: List[int]) -> int:
        subs = [[]]
        for e in nums:
            for sub in subs:
                if not sub or e > sub[-1]:
                    subs.append(sub + [e])
                    subs = sorted(subs, key=lambda x: -len(x))
                    break


        return len(subs[0])

# reflect:

# First I was able to write a brute force looking solution that was too slow, and then I improved the runtime.

# The brute force solution was a tree - construct every possible subsequence, and then look at all the subsequences to find the best one.

# Then I had to trim the tree. It felt sorta like house robber or best time to buy and sell stocks. By adding each element to only one subsequence, you enforce the constraint that you had only the best subsequence for each element. It feels a little bit like statistical mechanics or thermo as well - let us prudently decide what to hold constant and what to vary. Here we hold onto the best subsequence that DOES end with a given element. Sort of like the best path that DOES end with a given element. Its a little different because we are holding onto the best for the most recent element and earlier ones in a different way - they are in a list rather than elements in an array. I guess I could implement that way as well - it would be an array of arrays, each element being the longest array that includes that element. When it came time to add the next element, you would scan backwards and pick which one to choose. Yeah that would work. If you didn't find anything, you would add just itself. Ok so I see how this problem is equivalent to a trimmed tree traversal, and to implementations of house robber and best time to buy and sell stock. I think if implemented this solution in like my house robber solution, it would not be as evident that it was a tree traversal. Can I go implement house robber as a tree traversal?

# constructing trees with for loops is my desired method for constructng the tree.

# The improvement that made it into the first iteration was to disinclude the subsequences that were not increasing. As I construct subsequences, drop non-increasing subsequences. This resulted in the correct answer, but runtimes that were too long. So, to improve 1) dont check the entire sequence to see if it is increasing or not, just take a valid subsequence and add a larger number to it. 2) This is trickier, but it is alot like the house robber problem or the stocks problem. You only add each element once, and you add it to the longest list you can. This became apparent thinking about example sequences 2,3,4 and 3,4. There is no need to keep 3,4 , it will always get beet by this other sequence. I struggled to see how to implement this for a while. I could eventually visualize it as I was looking at the tree diagram that shows how all possible subsequences are generated. It is a moving left to right action that preferentially adds to the left, and not to lesser ones. It is important to leave the lesser ones there, as they will form their own distinct subsequences that must be considered. I had an idea to only add it to the longest one - that didn't really work out. Why? because 2, 3, 102, 103, 104, 4, 5, 6. I don't know how else to say it, other than you need to be very justified about when you trim this tree, lest you trim a subset that might be the longest subset. It makes sense to trim those subsequences that are shorter than others with the very same ending, that is justified and evident. Note that there is no actuall trimming in this implementation, only never-adding in the first place. The best summary of this solution is: build every possible subsequence by traversing a tree using a for loop. Start with all the subsequences for the empty list. Then find all the subsequences for the list containing only the first element by adding the first element to generate one new list, and by keeping the empty list. In this way, you have all the subsequences for the sequence of length 1. Capture all the subsequence for list of length k by keeping all the subsequences for list of length k-1, and adding element k to all the same subsequences. You now have twice as many subsequences, and all the subsequences for list of length k. Keep them all, and once you have all the subsequences for list of length n, then choose the greatest len(). This works but is not performant. To make it performant, be careful about which subsequences you are tracking. Tracking all guarentees that we can find the longest, but is there a subset that we can ignore and still find the longest? yea - all the subsets which end with a particular element (index), but shorter than another that ends with the same element (index). This can be implemented by only adding each element once - and to the subsequence that is longest. Ok so yeah, contrary to what I said earlier, we really are just adding a given element to the longest existing subsequnce. Note that this leaves the shortersubsequences which may have had the same start in-tact, and ready to be built upon with later elements. Does this really work? I think I just proved so above, but it might also help to think about what this is initialized with - the empty list, and that is never removed. So with every element we visit, we open up the possibility of starting a brand new sequence, if this new element happens to be too small to add to any existing sequences. ie. 100, 101, 102, 103, 104, 105, 106, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.