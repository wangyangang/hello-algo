
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ret = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []

        def func(node):
            if node is None:
                return
            func(node.left)
            ret.append(node.val)
            func(node.right)
        func(root)
        return ret


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.right = n2
    n2.left = n3
    s = Solution()
    ret = s.inorderTraversal(n1)
    print(ret)
