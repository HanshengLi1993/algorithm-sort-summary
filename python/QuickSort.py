# -*- coding: utf-8 -*-


def quick_sort(qlist):
    return qsort(qlist, 0, len(qlist) - 1)


def qsort(qlist, left, right):
    """
    快排函数
    :param qlist: 待排序数组
    :param left: 待排序的左边界
    :param right: 待排序的右边界
    :return:
    """
    if left >= right:
        return qlist
    key = qlist[left]  # 取最左边的为基准数
    lp = left  # 左指针
    rp = right  # 右指针
    while lp < rp:
        # 向右遍历数组，找比基准数小的数据的位置
        while qlist[rp] >= key and lp < rp:
            rp -= 1
        # 向左遍历数组，找比基准数大的数据的位置
        while qlist[lp] <= key and lp < rp:
            lp += 1
        # 以基准数为标准将比基准数小的数据放在左边，大的放右边
        qlist[lp], qlist[rp] = qlist[rp], qlist[lp]
    # 将基准数插入到左右分界点中，此时基准数左边的数据都比基准数小，右边数据都比基准数大
    qlist[left], qlist[lp] = qlist[lp], qlist[left]
    # 递归左右，将两边按上述方法排序直至整个数组有序
    qsort(qlist, left, lp - 1)
    qsort(qlist, rp + 1, right)
    return qlist


if __name__ == '__main__':
    qlist = quick_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(qlist)
