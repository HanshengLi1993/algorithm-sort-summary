# -*-coding:utf-8 -*-


def shell_sort(slist):
    length = len(slist)
    gap = round(length / 2)  # 初始化步长，用round四舍五入取整
    while gap > 0:
        for i in range(gap, length):  # 每一列进行插入排序，从 gap 到 length-1
            minPoint = slist[i]  # 在当前步长下做插入排序时最小数据指针
            j = i  # 在当前步长下做插入排序数据位移指针，指向下个数据的位置
            # 插入排序开始
            while j >= gap and slist[j - gap] > minPoint:  # 使用while为了保证j -= gap 后人能保持 j >= gap 时插入排序能继续执行下去，遍历所有所需数据
                slist[j] = slist[j - gap]
                j -= gap  # 保证插入排序
            slist[j] = minPoint
            # 插入排序结束
        gap = round(gap / 2)  # 重设置步长
    return slist


if __name__ == '__main__':
    slist = shell_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(slist)
