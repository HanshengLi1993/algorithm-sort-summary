# -*- coding: utf-8 -*-


def merge_sort(mlist):
    if len(mlist) <= 1:
        return mlist
    mid = int(len(mlist) / 2)
    # 使用递归将数组二分分解
    left = merge_sort(mlist[:mid])
    right = merge_sort(mlist[mid:])
    return merge(left, right)  # 将每次分解出来的数组各自排序，合并成一个大数组


def merge(left, right):
    """
    合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组
    :param left:
    :param right:
    :return:
    """
    l, r = 0, 0  # left与right数组的下标指针
    result = []
    while l < len(left) and r < len(right):
        # 排序
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


if __name__ == '__main__':
    mlist = merge_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(mlist)
