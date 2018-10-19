# -*-coding:utf-8 -*-


def insert_sort(ilist):
    for i in range(len(ilist)):
        for j in range(i):
            if ilist[i] < ilist[j]:
                ilist.insert(j, ilist.pop(i))  # pop()方法的返回值是被移除元素的值
                break
    return ilist


if __name__ == '__main__':
    ilist = insert_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
    print(ilist)
