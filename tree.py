"""these are basic exercises with linked list trees and graphs"""


class N:

    def __init__(self, value, left, rite):
        self.value: int = value
        self.left: N = left
        self.rite: N = rite


"""
       1
   2       3
 4   5   6   7
"""

a = N(
    1,
    N(2, N(4, None, None), N(5, None, None)),
    N(
        3,
        N(6, None, None),
        N(7, None, None),
    ),
)


"""I am confused about how to traverse a tree, with a loop. Do you need an external list or stack or something like that?yeah when you have the reference to cur, that is the last time you can go both directions. So the simplest thing is to print the cur value, and then add the two to a list, and then pop from the list?"""

msg = """
by-level schriftlich traversal, with a loop
"""
print(msg)
hold = [a]
while hold:
    cur = hold.pop(0)
    print(cur.value)
    if cur.left:
        hold.append(cur.left)
    if cur.rite:
        hold.append(cur.rite)

msg = """
by-level reverse traversal, with a loop
"""
print(msg)
hold = [a]
while hold:
    cur = hold.pop(0)
    print(cur.value)
    if cur.rite:
        hold.append(cur.rite)
    if cur.left:
        hold.append(cur.left)


msg = """
right traversal, with a loop
"""
print(msg)
hold = [a]
while hold:
    cur = hold.pop()
    print(cur.value)
    if cur.left:
        hold.append(cur.left)
    if cur.rite:
        hold.append(cur.rite)

msg = """
left traversal, with a loop
"""
print(msg)
hold = [a]
while hold:
    cur = hold.pop()
    print(cur.value)
    if cur.rite:
        hold.append(cur.rite)
    if cur.left:
        hold.append(cur.left)


msg = """
in-order traversal (recursive)
"""
print(msg)


def visit(node) -> None:
    if not node:
        return
    visit(node.left)
    print(node.value)
    visit(node.rite)


visit(a)


msg = """
pre-order traversal (recursive)
"""
print(msg)


def visit(node) -> None:
    if not node:
        return
    print(node.value)
    visit(node.left)
    visit(node.rite)


visit(a)


msg = """
post-order traversal (recursive)
"""
print(msg)


def visit(node) -> None:
    if not node:
        return
    visit(node.left)
    visit(node.rite)
    print(node.value)


visit(a)
