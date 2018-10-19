# -*- coding: utf-8 -*-


def counting_sort(clist):
    # 构造桶
    bucketLength = max(clist) + 1
    bucket = [0] * bucketLength

    sortedIndex = 0
    length = len(clist)
    # 将元素装入桶中，对应桶的数量加一表示该桶中相同数据的数量
    for i in range(length):
        if not bucket[clist[i]]:
            bucket[clist[i]] = 0
        bucket[clist[i]] += 1

    # 将桶中元素去除，并填充到有序数组中
    for j in range(bucketLength):
        while bucket[j] > 0:
            clist[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return clist


if __name__ == '__main__':
    clist = counting_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(clist)
