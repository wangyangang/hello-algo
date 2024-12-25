def move(src, tar):
    item = src.pop()
    tar.append(item)


def dfs(i, src, buff, tar):
    # src柱子上的i个环，借助buff柱子移动到tar上
    if i == 1:
        move(src, tar)
        return
    dfs(i-1, src, tar, buff)
    move(src, tar)
    dfs(i-1, buff, src, tar)


def solve_hanota(A, B, C):
    i = len(A)
    dfs(i, A, B, C)


"""Driver Code"""
if __name__ == "__main__":
    # 列表尾部是柱子顶部
    A = [5, 4, 3, 2, 1]
    B = []
    C = []
    print("初始状态下：")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")

    solve_hanota(A, B, C)

    print("圆盘移动完成后：")
    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")