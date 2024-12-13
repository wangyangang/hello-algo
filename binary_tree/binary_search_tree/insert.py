from binary_tree.tree import Node
#               8
#       4               12
#   2      6       10         14
# 1   3  5   7   9    11   13     15
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)
n12 = Node(12)
n13 = Node(13)
n14 = Node(14)
n15 = Node(15)
n8.left = n4
n8.right = n12
n4.left = n2
n4.right = n6
n2.left = n1
n2.right = n3
n6.left = n5
n6.right = n7
n12.left = n10
n12.right = n14
n10.left = n9
n10.right = n11
n14.left = n13
n14.right = n15

from binary_tree.traverse_binary_tree.binary_tree_bfs import bfs
ret = bfs(n8)
# [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
print(ret)

# insert 16
def insert(root, num):
    if root is None:
        root = Node(num)
        return
    current = root
    pre = current
    while current is not None:
        if num > current.val:
            pre = current
            current = current.right
        else:
            pre = current
            current = current.left
    if num > pre.val:
        pre.right = Node(num)
    else:
        pre.left = Node(num)


if __name__ == '__main__':
    insert(n8, 16)
    ret = bfs(n8)
    print(ret)

    insert(None, 16)
    ret = bfs(None)
    print(ret)
