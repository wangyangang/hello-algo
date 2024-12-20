def find_mid(nums, left, right):
    i, j = left, right
    while i < j:
        # 从右向左找到首个小于基准数的元素
        while i < j and nums[j] >= nums[left]:
            j -= 1
        # 从左向右找到首个大于基准数的元素
        while i < j and nums[i] <= nums[left]:
            i += 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[left], nums[i] = nums[i], nums[left]
    return i


def quick_sort(nums, left, right):
    # 子数组长度为1时，终止递归
    if left >= right:
        return
    mid = find_mid(nums, left, right)
    # 递归左子树组
    quick_sort(nums, left, mid-1)
    # 递归右子树组
    quick_sort(nums, mid+1, right)


if __name__ == '__main__':
    # 快速排序
    nums = [2, 4, 1, 0, 3, 5]
    quick_sort(nums, 0, len(nums) - 1)
    print("快速排序完成后 nums =", nums)