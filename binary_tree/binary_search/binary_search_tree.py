from binary_tree.tree import Node
#       4
#   2      6
# 1   3  5   7
n4 = Node(4)
n2 = Node(2)
n6 = Node(6)
n1 = Node(1)
n3 = Node(3)
n5 = Node(5)
n7 = Node(7)
n4.left = n2
n4.right = n6
n2.left = n1
n2.right = n3
n6.left = n5
n6.right = n7

# 根据节点的值，查找到节点  递归的方法
def binary_search1(node, val):
    if node is None:
        return None
    if node.val == val:
        return node
    if val < node.val:
        return binary_search1(node.left, val)
    if val > node.val:
        return binary_search1(node.right, val)

# 循环的方法
def binary_search2(node, val):
    if node.val == val:
        return node
    while node is not None:
        if node.val == val:
            return node
        elif val > node.val:
            node = node.right
        else:
            node = node.left
    return None


if __name__ == '__main__':
    ret = binary_search2(n4,5)
    print(ret)
    if ret:
        print(ret.val)