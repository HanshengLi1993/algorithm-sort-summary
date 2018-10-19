# -*- coding: utf-8 -*-


def bucket_sort(blist, bucketSize=5):
    length = len(blist)
    if length == 0:
        return blist

    minValue = maxValue = blist[0]
    for i in range(length):
        if blist[i] < minValue:
            minValue = blist[i]  # 数组中的最小值
        elif blist[i] > maxValue:
            maxValue = blist[i]  # 数组中的最大值

    # 初始化桶
    bucketCount = int((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(bucketCount):
        buckets.append([])

    # 利用映射函数将数据分配到各个桶中
    for i in range(length):
        buckets[int((blist[i] - minValue) / bucketSize)].append(blist[i])

    # 将排序好的数据装入并返回
    sort_list = []
    for i in range(bucketCount):
        insert_sort(buckets[i])  # 对个桶进行排序，list并不在函数调用结束后就释放资源。当它作为函数参数时，相当于全局变量，在函数预处理时就已经分配了内存空间
        for j in range(len(buckets[i])):
            sort_list.append(buckets[i][j])
    return sort_list


def insert_sort(ilist):
    for i in range(len(ilist)):
        for j in range(i):
            if ilist[i] < ilist[j]:
                ilist.insert(j, ilist.pop(i))  # pop()方法的返回值是被移除元素的值
                break
    return ilist


if __name__ == '__main__':
    blist = bucket_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(blist)
