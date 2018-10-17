# -*- coding: utf-8 -*-


def radix_sort(rlist):
    # 选择一个最大的数
    max_num = max(rlist)
    # 创建一个元素全是0的列表，当作桶
    bucket = [0] * (max_num + 1)

    # 把所有元素放入桶中，即把对应元素个数加一
    for i in rlist:
        bucket[i] += 1
    # 存储排序好的元素
    sort_nums = []
    # 取出桶中的元素
    for j in range(len(bucket)):
        if bucket[j] != 0:
            for y in range(bucket[j]):
                sort_nums.append(j)
    return sort_nums


if __name__ == '__main__':
    rlist = radix_sort([5, 6, 3, 2, 1, 65, 2, 0, 8, 0, 11])
    print(rlist)
