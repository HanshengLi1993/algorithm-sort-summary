# -*- coding: utf-8 -*-


def counting_sort(clist):
    bucketLength = max(clist) + 1
    bucket = [0] * bucketLength
    sortedIndex = 0
    length = len(clist)
    for i in range(length):
        if not bucket[clist[i]]:
            bucket[clist[i]] = 0
        bucket[clist[i]] += 1

    for j in range(bucketLength):
        while bucket[j] > 0:
            clist[sortedIndex] = j
            sortedIndex += 1
            bucket[j] -= 1
    return clist


if __name__ == '__main__':
    clist = counting_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(clist)
