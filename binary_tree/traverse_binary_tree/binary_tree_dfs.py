# 深度优先的遍历 dfs通常使用递归
# 分为前序、中序和后续三种顺序

res = []
# 前序
def pre_order(node):
    # 访问顺序：父节点，左子树，右子树
    res.append(node.val)
    if node.left:
        pre_order(node.left)
    if node.right:
        pre_order(node.right)

# 中序
def in_order(node):
    # 访问顺序：左子树-父节点-右子树
    if node.left:
        in_order(node.left)
    res.append(node.val)
    if node.right:
        in_order(node.right)

# 后序
def post_order(node):
    # 访问顺序： 左子树-右子树-父节点
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)
    res.append(node.val)


if __name__ == '__main__':
    from binary_tree.tree import root
    post_order(root)
    print(res)