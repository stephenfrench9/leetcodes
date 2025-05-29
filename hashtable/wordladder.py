# https://leetcode.com/problems/word-ladder/submissions/1646950224/?envType=problem-list-v2&envId=hash-table

"""
check every word in the wordList evrytime.

this first solution actually passes. the run time is O(solutionlength*wordlist)
beats 5%
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        words = set([beginWord])
        if beginWord in wordList:
            wordList.remove(beginWord)
        trans = 1

        while words:
            # print(words, wordList)
            next_words = set()
            for cur in words:
                for cand in wordList:
                    disagrees = [c != d for c, d in zip(cur, cand)].count(True)
                    if disagrees == 1:
                        next_words.add(cand)
            for next_word in next_words:
                wordList.remove(next_word)
            # print(next_words)
            words = next_words
            trans += 1
            if endWord in words:
                return trans
            # print()

        return 0


print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))


from collections import defaultdict


class Solution0:
    """
    Poor implementation of fuzzy search

    This solution is slow. I tried to speed up the algorithm by using a hashmap to check if a given transition was valid. The idea is to convert each word (current position) into fuzzy forms, and then look up those fuzzy forms in a dict. This way you get 3 dict lookups instead of iterating over an entire list and trying to find elements that are different in only one position. The net effect was that the entire thing did not work. Oh wait, I wrote that crazy wrong. What did I write? There is still the full iteration over the entire word list, and then I check for every candidate, I compute all the fuzzy forms, and then look them up in the longforms, and then see if the candidate is in the fuzzy forms. So I still have the entire iteration. On the bright side, the final iteration is looking pretty tight.

    times out
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        global longform
        global SPECIAL
        SPECIAL = ")"

        # initialize a helper for a fuzzy search
        longform = defaultdict(list)
        for w in wordList:
            w_star = list(w)
            for i, c in enumerate(w_star):
                w_star[i] = SPECIAL
                longform["".join(w_star)].append(w)
                w_star[i] = c

        def valid(cand, word):
            # print(word, ' -> ', cand, '?')
            word_star = list(word)
            for i, ch in enumerate(word_star):
                # print('i: ',i,'ch: ', ch)
                word_star[i] = SPECIAL
                # print('word_star: ', word_star)
                fuzzy = "".join(word_star)
                # print('fuzzy: ', fuzzy)
                word_star[i] = ch
                if fuzzy in longform:
                    # print('there is longform[fuzzy]')
                    # print('cand: ', cand, '  longform[fuzzy]: ', longform[fuzzy])
                    if cand in longform[fuzzy]:
                        # print('TTTTTRRRRRUUUUUEEEE')
                        # print()
                        return True
                # print()

        """
        def valid(cand, word):
            disagrees = [c != d for c, d in zip(cur, cand)].count(True)
            if disagrees == 1:
                return True
        """
        # words controls the iteration, it is the current position
        words = set([beginWord])
        if beginWord in wordList:
            wordList.remove(beginWord)
        # length of transition sequence
        leng = 1

        while words:
            print("loop control: ", words)
            next_words = set()
            for cur in words:
                for cand in wordList:
                    if valid(cand, cur):
                        next_words.add(cand)
            for next_word in next_words:
                wordList.remove(next_word)

            words = next_words
            leng += 1
            if endWord in words:
                return leng
            print()

        return 0


class Solution1:
    """
    fuzzy search

    for fuzzy of word:
        longforms[fuzzy]
    -> Take a word, compute all the fuzzy forms, then look each of the fuzzy forms up in a dictionary to find all the longforms that they can map to.

    each step is a set of words. find all the next_words for each word. update words. You dont want to visit the same word twice. It could lead to a loop, or just be slower.
    Note: To protect against this, I empty out all the target words for each fuzzy form when I take them. It guarantees no loops, because it empties out all the transitions for every word, because given a word, you find fuzzies, and then if I eliminate the fuzzies, it means that if this word is every reintroduced to the current step state (by a different fuzzy word probably), it can't lead anywhere.


    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        global longform
        global SPECIAL
        SPECIAL = ")"

        # initialize a helper for a fuzzy search
        longform = defaultdict(list)
        for w in wordList:
            w_star = list(w)
            for i, c in enumerate(w_star):
                w_star[i] = SPECIAL
                longform["".join(w_star)].append(w)
                w_star[i] = c

        # 'words' controls the iteration, it is the current position
        words = set([beginWord])
        if beginWord in wordList:
            wordList.remove(beginWord)

        # length of transition sequence
        leng = 1

        while words:
            print("loop control: ", words)
            next_words = set()
            for cur in words:
                cur_star = list(cur)
                for i, c in enumerate(cur_star):
                    cur_star[i] = SPECIAL
                    new_next_words = longform["".join(cur_star)]
                    for new_next_word in new_next_words:
                        next_words.add(new_next_word)
                    longform["".join(cur_star)] = []
                    cur_star[i] = c

            words = next_words - words  # - words is not technically needed.

            leng += 1
            if endWord in words:
                return leng

        return 0


class Solution2:
    """
    no fuzzy search, but precompute a map

    could I precompute a super helpful map, that is just all the targets given a word?

    timesout
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        targets = defaultdict(list)
        for word in [*wordList, beginWord]:
            for target in wordList:
                if [w != t for w, t in zip(word, target)].count(True) == 1:
                    targets[word].append(target)
        words = {beginWord}
        leng = 1

        while words:
            next_words = set()

            for word in words:
                next_words.update(targets[word])
                targets[word] = []

            words = next_words
            leng += 1

            if endWord in words:
                return leng

        return 0


class Solution3:
    """
    precompute a map efficiently, using a fuzzy mapping to relate words. Rather than checking every pair, I look at each word, and map it to something, and then words that mapped to the same thing go together so you don't have to look at every pair. This is fuzzy mapping into groups of similiar items, rather than considering every pair to see if they can be grouped together. This is probably basically what you did above too, except partially in the action.

    lets try to precompute the map more efficiently

    # update method on sets is nice, like the extend method on lists.
    """

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        fuzz_targets = defaultdict(list)
        beginWordTargets = (
            []
        )  # you could just lump beginWord into wordList, but this is more efficient from a compute perspective, at the expense of some extra code.

        for word in wordList:
            if [b != w for b, w in zip(beginWord, word)].count(True) == 1:
                beginWordTargets.append(word)

            for i in range(len(word)):
                fuzzy = word[:i] + "(" + word[i + 1 :]
                fuzz_targets[fuzzy].append(word)

        targets = defaultdict(list)
        for fuzzy, words in fuzz_targets.items():
            for word in words:
                targets[word].extend(words)
                targets[word].remove(word)
        targets[beginWord] = beginWordTargets

        words = {beginWord}
        leng = 1

        while words:
            next_words = set()

            for word in words:
                next_words.update(targets[word])
                targets[word] = []

            words = next_words
            leng += 1

            if endWord in words:
                return leng

        return 0
