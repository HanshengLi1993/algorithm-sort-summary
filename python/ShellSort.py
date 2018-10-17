# -*-coding:utf-8 -*-


def shell_sort(slist):
    length = len(slist)
    gap = round(length / 2)  # 初始化步长，用round四舍五入取整
    while gap > 0:
        for i in range(gap, length):  # 每一列进行插入排序，从 gap 到 n-1
            temp = slist[i]
            j = i
            while j >= gap and slist[j - gap] > temp:  # 插入排序
                slist[j] = slist[j - gap]
                j -= gap
            slist[j] = temp
        gap = round(gap / 2)  # 重设置步长
    return slist


if __name__ == '__main__':
    slist = shell_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(slist)
