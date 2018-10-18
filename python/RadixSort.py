# -*- coding: utf-8 -*-


def radix_sort(rlist, radix=10):
    length = len(rlist)
    if rlist is None or length < 2:
        return rlist
    maxValue = max(rlist)
    maxDigit = 0
    while maxValue != 0:
        maxValue //= 10  # python3里的"/"表示 浮点数除法,返回浮点结果,"//"表示整数除法
        maxDigit += 1
    mod = radix
    div = 1
    bucketList = []
    for i in range(mod):
        bucketList.append([])
    for i in range(maxDigit):
        for j in range(length):
            num = int((rlist[j] % mod) / div)
            bucketList[num].append(rlist[j])
        index = 0
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
