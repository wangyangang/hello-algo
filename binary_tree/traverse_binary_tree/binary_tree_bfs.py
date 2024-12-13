# 层序遍历
from binary_tree.tree import Node, root
from collections import deque

# 广度优先的遍历采用 “队列” 来实现
def bfs(node=None):
    q = deque([node])
    ret = []
    while q:
        item = q.pop()
        if item is not None:
            ret.append(item.val)
            if item.left:
                q.appendleft(item.left)
            if item.right:
                q.appendleft(item.right)
    return ret

if __name__ == '__main__':
    bfs(root)
