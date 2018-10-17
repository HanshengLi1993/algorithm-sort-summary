# -*- coding: utf-8 -*-


def quick_sort(qlist):
    return qsort(qlist, 0, len(qlist) - 1)


def qsort(ary, left, right):
    """
    快排函数
    :param ary: 待排序数组
    :param left: 待排序的左边界
    :param right: 待排序的右边界
    :return:
    """
    if left >= right:
        return ary
    key = ary[left]  # 取最左边的为基准数
    lp = left  # 左指针
    rp = right  # 右指针
    while lp < rp:
        while ary[rp] >= key and lp < rp:
            rp -= 1
        while ary[lp] <= key and lp < rp:
            lp += 1
        ary[lp], ary[rp] = ary[rp], ary[lp]
    ary[left], ary[lp] = ary[lp], ary[left]
    qsort(ary, left, lp - 1)
    qsort(ary, rp + 1, right)
    return ary
