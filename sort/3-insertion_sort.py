# 插入排序类似于整理扑克牌，从后面未排序的牌里拿出第一张（base），与前面已经拍好的做比较。
# 从拍好的牌里从后往前比较，如果拍好的牌里的牌，大于base，则把拍好的牌后移，最后j的牌，是小于等于base的牌。
# 那么把j+1的位置赋予base即可。
def insertion_sort(nums):
    for i in range(1, len(nums)):
        base = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > base:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = base


"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    insertion_sort(nums)
    print("冒泡排序完成后 nums =", nums)