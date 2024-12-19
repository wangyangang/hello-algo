


def binary_search(nums, target):
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1
    while left <= right:
        m = (left + right) // 2
        if nums[m] == target:
            return m
        if nums[m] > target:
            right = m - 1
        else:
            left = m + 1
    return left


"""Driver Code"""
if __name__ == "__main__":
    target =4
    nums = [1]

    # 二分查找（双闭区间）
    index = binary_search(nums, target)
    print("目标元素 4 的插入位置 = ", index)