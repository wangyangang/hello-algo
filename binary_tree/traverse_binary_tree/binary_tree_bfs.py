# 层序遍历
from binary_tree.tree import Node, root
from collections import deque


def bfs(node=None):
    q = deque([node])
    while q:
        item = q.pop()
        print(item.val)
        if item.left:
            q.appendleft(item.left)
        if item.right:
            q.appendleft(item.right)


if __name__ == '__main__':
    bfs(root)
