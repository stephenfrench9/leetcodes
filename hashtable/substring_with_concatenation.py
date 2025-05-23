# https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=problem-list-v2&envId=hash-table
from collections import Counter


class Solution0:
    """
    problem statement, and definitions of some important terms.

    - 'The string', 's', refers to the input string.
    - 'substring' refers to a substring of 'the string'.
    - 'words' is a list of words, which are all of length l.
    - 'concatenations', or 'cats', are permutations of all the 'words'.
    - the task is to look for 'cats' in 'The String'.

    strategy: traverse the string S from index 'ind' optimistically, searching for substrings of length l in the list words to determine if it is possible to advance, and continunig until you can't find the current substring in the words or you 'pos' is off the end of the string. (depending on what happens when slice a string at too large indices and then compare to other strings, maybe you don't even need to worry about position). Then evaluate the traversal in order to decide if the index ind is the start of a 'cat'.

    - 'ind' refers to starting positions of the traversal.
    - 'pos' refers to a position or index of the string in the context of a traversal across the string.

    too slow
    """

    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        outputs: list[int] = []
        l: int = len(words[0])
        for ind in range(len(s)):
            remaining = list(words)
            pos: int = ind
            cur: str = s[pos : pos + l]
            while cur in remaining:  # and pos < len(s):
                remaining.remove(cur)
                pos += l
                cur = s[pos : pos + l]
            if not remaining:  # and pos<=len(s):
                outputs.append(ind)
        return outputs


"""
problem statement, and definitions of some important terms.

- 'The string', 's', refers to the input string.
- 'substring' refers to a substring of 'the string'.
- 'words' is a list of words, which are all of length l. there are k words. A cat is k*l long
- 'concatenations', or 'cats', are permutations of all the 'words'.
- the task is to look for 'cats' in 'The String'.

strategy: a traversal from 'ind' and from 'ind' + 1 are not related to each other, the words are completely different. But the traversals from 'ind' and 'ind' + l are related. the potential cat starting at ind + l would have the same words, except for having an extra word at the end and missing a word at the front. So have a counter dict of all the remaining words which were not used for the traversal from ind (maybe it is empty). Then to know if there is traversal or a cat starting at ind + l, add the substring s[ind: ind + l] back to the dict, and remove the substring s[ind+k*l:ind+ k*l +l], now you know.

How will this be structured in code? It must be done for each seed in [0:l] (a new word starts a l). And the cats starting at multiples of l will be considered. The full traversal must be done for the initial traversal, and then proceed into a loop to raster the starting position across the string. At then end of each traversal, the starting position ind must be either recorded or not as the start of a cat. Ill let seed refer to the indices where the full traversal is done, and ind to starting positions of derivative traversals. 

- 'ind' refers to starting positions of the traversal.
- 'pos' refers to a position or index of the string in the context of a traversal across the string.

"""


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        from collections import Counter

        if not s or not words:
            return []
        cats: list[int] = []
        l: int = len(words[0])
        k: int = len(words)
        required: Counter = Counter(words)

        for seed in range(l):
            candidate: list[str] = [s[i : i + l] for i in range(seed, seed + l * k, l)]

            available: Counter = Counter(candidate)

            if required == available:
                cats.append(seed)

            ind: int = seed + l
            while ind <= len(s):
                expired_word: str = s[ind - l : ind]
                new_word: str = s[ind + l * k - l : ind + l * k]
                available.update({expired_word: -1})
                available.update({new_word: 1})
                if available == required:
                    cats.append(ind)
                ind += l

        return cats


s = "barfoothefoobarman"
words: list[str] = ["foo", "bar"]

a = Solution()
result = a.findSubstring(s, words)
print(result)

"""
pos: int = seed
cur: str = s[pos:pos+l]
while cur in remaining:
    remaining.remove(cur)
    pos+=l
    cur: str = s[pos:pos+l]             
if not remaining:
    cats.append(seed)
ind: int = seed + l
while ind < len(s):
    remaining.add(s[ind-l:ind])
    remaining.remove(s[ind+k*l-l:ind+k*l])
    if not remaining:
        cats.append(ind)
    ind += l

return cats
"""
