# -*-coding:utf-8 -*-


def bubble_sort_v1(blist):
    length = len(blist)
    for i in range(length):
        for j in range(1, length - 1):
            if blist[j - 1] > blist[j]:
                blist[j - 1], blist[j] = blist[j], blist[j - 1]
    return blist


def bubble_sort_v2(blist):
    """
    优化1：在某一趟遍历中没有数据发生交换，则说明排序已经完成，不需要继续遍历
    :param blist:
    :return:
    """
    length = len(blist)
    for i in range(length):
        flag = True
        for j in range(1, length - 1):
            if blist[j - 1] > blist[j]:
                blist[j - 1], blist[j] = blist[j], blist[j - 1]
                flag = False
        if flag:
            break
    return blist


def bubble_sort_v3(blist):
    """
    优化2：记录某次遍历时最后发生数据交换的位置，从这个位置起之后的数据已然有序
    :param blist:
    :return:
    """
    endPoint = length = len(blist)
    for i in range(length):
        flag = True  # 判断数据在本次遍历中是否交换过，若未发生交换，则余下的数据已经排好序，算法完成
        for j in range(1, endPoint):  # endPoint为上次最后发生数据交换的位置
            if blist[j - 1] > blist[j]:
                blist[j - 1], blist[j] = blist[j], blist[j - 1]
                endPoint = j  # 记录每次发生数据交换的位置
                flag = False
        if flag:
            break
    return blist


if __name__ == '__main__':
    blist = bubble_sort_v3([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(blist)
