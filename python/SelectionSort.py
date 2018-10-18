# -*-coding:utf-8 -*-


def select_sort(slist):
    for i in range(len(slist)):
        minPoint = i  # minPoint本次遍历最小数据指针
        for j in range(i, len(slist)):
            if slist[j] < slist[minPoint]:
                minPoint = j
        slist[i], slist[minPoint] = slist[minPoint], slist[i]  # 将最小数据交换到本次遍历 头部
    return slist


if __name__ == '__main__':
    slist = select_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(slist)
