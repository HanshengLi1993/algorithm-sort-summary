# -*- coding: utf-8 -*-


def merge_sort(mlist):
    if len(mlist) <= 1:
        return mlist
    num = int(len(mlist) / 2)  # 二分分解
    left = merge_sort(mlist[:num])
    right = merge_sort(mlist[num:])
    return merge(left, right)  # 合并数组


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
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
