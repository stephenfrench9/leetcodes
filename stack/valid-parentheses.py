class Solution:
    def isValid(self, s: str) -> bool:
        stack = ['}']
        for ss in s:
            if ss in ('{', '(', '['):
                stack.append(ss)
            else:
                openphrase = stack.pop()
                if openphrase + ss not in ('()', '[]', '{}'):
                    return False

        return len(stack) == 1
