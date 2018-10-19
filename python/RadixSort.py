# -*- coding: utf-8 -*-


def radix_sort(rlist, radix=10):
    """

    :param rlist:待排序数组
    :param radix: 基数
    :return:
    """
    length = len(rlist)
    if rlist is None or length < 2:
        return rlist
    maxValue = max(rlist)
    maxDigit = 0
    # 获取数组最大值的位数
    while maxValue != 0:
        maxValue //= 10  # python3里的"/"表示 浮点数除法,返回浮点结果,"//"表示整数除法
        maxDigit += 1
    mod = radix
    div = 1
    # 初始化桶
    bucketList = []
    for i in range(mod):
        bucketList.append([])
    for i in range(maxDigit):
        # 将数据按从低到高位，从各位开始逐层向上排序，并按排序的位将数据装入桶中得到此位数据有序
        for j in range(length):
            num = int((rlist[j] % mod) / div)
            bucketList[num].append(rlist[j])
        index = 0
        # 将基数桶中的数据取出，得到部分有序的数组
        for j in range(len(bucketList)):
            for k in range(len(bucketList[j])):
                rlist[index] = bucketList[j][k]
                index += 1
        mod *= 10
        div *= 10
    return rlist


if __name__ == '__main__':
    rlist = radix_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(rlist)
