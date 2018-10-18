# -*- coding: utf-8 -*-


def heap_sort(hlist):
    length = len(hlist)
    first = int(length / 2 - 1)  # 最后一个非叶子节点
    for start in range(first, -1, -1):  # 构造大根堆
        max_heapify(hlist, start, length - 1)  # 由于列表的浅拷贝，hlist已经是大根堆
    for end in range(length - 1, 0, -1):  # 堆排，将大根堆转换成有序数组
        # 将大根堆的根节点交换到最后，并排除到排序之外
        hlist[end], hlist[0] = hlist[0], hlist[end]
        # 继续构造大根堆
        max_heapify(hlist, 0, end - 1)
    return hlist


def max_heapify(hlist, start, end):
    """
    最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
    :param hlist:
    :param start: 当前需要调整最大堆的位置
    :param end: 调整边界
    :return:
    """
    root = start  # 选取根节点
    while True:
        child = root * 2 + 1  # 调整节点的子节点
        if child > end:
            break
        if child + 1 <= end and hlist[child] < hlist[child + 1]:
            child += 1  # 取较大的子节点
        if hlist[root] < hlist[child]:  # 较大的子节点成为父节点
            hlist[root], hlist[child] = hlist[child], hlist[root]  # 交换
            root = child  # 将子节点当作下一层的父节点，继续选取子节点
        else:
            break


if __name__ == '__main__':
    hlist = heap_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(hlist)
