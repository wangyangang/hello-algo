def binary_search(nums: list[int], target: int) -> int:
    """二分查找（双闭区间）"""
    # 初始化双闭区间 [0, n-1] ，即 i, j 分别指向数组首元素、尾元素
    i, j = 0, len(nums) - 1
    # 循环，当搜索区间为空时跳出（当 i > j 时为空）
    while i <= j:
        # 理论上 Python 的数字可以无限大（取决于内存大小），无须考虑大数越界问题
        m = (i + j) // 2  # 计算中点索引 m
        if nums[m] < target:
            i = m + 1  # 此情况说明 target 在区间 [m+1, j] 中
        elif nums[m] > target:
            j = m - 1  # 此情况说明 target 在区间 [i, m-1] 中
        else:
            return m  # 找到目标元素，返回其索引
    return -1  # 未找到目标元素，返回 -1


def binary_search2(nums, target):
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    while left < right:
        m = (left + right) // 2
        if nums[m] == target:
            return m
        if nums[m] > target:
            right = m - 1
        else:
            left = m + 1
    return -1


"""Driver Code"""
if __name__ == "__main__":
    target = 1
    nums = [1, 2, 3, 4, 5]

    # 二分查找（双闭区间）
    index = binary_search(nums, target)
    print("目标元素 6 的索引 = ", index)