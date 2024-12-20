# 归并排序
def merge(nums, left, mid, right):
    """合并左子数组和右子数组"""
    # 左子数组区间为 [left, mid]， 右子数组区间为 [mid+1, right]
    # 初始化左子树组和右子数组的索引
    i = left
    j = mid + 1
    k = 0
    # 创建一个临时数组tmp，用于存放合并后的数据
    tmp = [0] * (right - left + 1)
    # 当左右子数组都还有元素时，进行比较并把较小的数据复制到临时数组中
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1
    # 将左子数组和右子数组的剩余元素复制到临时数组中
    while i <= mid:
        tmp[k] = nums[i]
        i += 1
        k += 1
    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1
    # 将临时数组tmp中的元素复制回原数组nums的对应区间
    for idx in range(k):
        nums[left + idx] = tmp[idx]


def merge_sort(nums, left, right):
    if left >= right:
        return
    mid = (left + right) // 2
    merge_sort(nums, left, mid)
    merge_sort(nums, mid+1, right)
    merge(nums, left, mid, right)


if __name__ == '__main__':
    nums = [7, 3, 2, 6, 0, 1, 5, 4]
    merge_sort(nums, 0, len(nums) - 1)
    print("归并排序完成后 nums =", nums)