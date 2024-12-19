def bubble_sort(nums):
    for i in range(len(nums) - 1, -1, -1):
        for j in range(i):
            if nums[j+1] < nums[j]:
                nums[j+1], nums[j] = nums[j], nums[j+1]


"""Driver Code"""
if __name__ == "__main__":
    nums = [4, 1, 3, 1, 5, 2]
    bubble_sort(nums)
    print("冒泡排序完成后 nums =", nums)