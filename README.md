#                     		十大经典排序算法-Python实现

## 算法概述

### 算法分类

十种经典排序算法可分为俩大类：

**非线性时间比较类排序**：通过比较来决定元素之间的相互次序，由于起事件负载都不能突破O(n log n)，因此被称为非线性时间比较类排序。

**线性时间非比较类排序**：不通过比较来决定元素之间的次序，它可以突破给予比较排序的时间下届，以线性时间运行，因此被称为线性时间非比较类排序。

- 比较排序的优势是，适用于各种规模的数据，也不在乎数据的分布，都能进行排序。可以说，比较排序适用于一切需要排序的情况。
- 非比较排序只要确定每个元素之前的已有的元素个数即可，所有一次遍历即可解决。算法时间复杂度O(n)。非比较排序时间复杂度底，但由于非比较排序需要占用空间来确定唯一位置。所以对数据规模和数据分布有一定的要求。

![]()

### 算法复杂度

| **排序方法** | **平均时间复杂度** | **最好时间复杂度** | **最坏时间复杂度** | **空间复杂度** | **排序方式** | **稳定性** |
| :----------: | :----------------: | :----------------: | :----------------: | :------------: | ------------ | :--------: |
|   冒泡排序   |      O(n^2^)       |        O(n)        |      O(n^2^)       |      O(1)      | In-place     |    稳定    |
|   快速排序   |     O(n log n)     |     O(n log n)     |      O(n^2^)       | O(log n)~O(n)  | In-place     |   不稳定   |
|   插入排序   |      O(n^2^)       |        O(n)        |      O(n^2^)       |      O(1)      | In-place     |    稳定    |
|   希尔排序   | O(n log n)~O(n^2^) |     O(n^1.3^)      |        O(n)        |      O(1)      | In-place     |   不稳定   |
|   选择排序   |      O(n^2^)       |      O(n^2^)       |      O(n^2^)       |      O(1)      | In-place     |   不稳定   |
|    堆排序    |     O(n log n)     |     O(n log n)     |     O(n log n)     |      O(1)      | In-place     |   不稳定   |
|   归并排序   |     O(n log n)     |     O(n log n)     |     O(n log n)     |      O(n)      | Out-place    |    稳定    |
|              |                    |                    |                    |                |              |            |
|    桶排序    |       O(n+k)       |       O(n+k)       |      O(n^2^)       |     O(n+k)     | Out-place    |    稳定    |
|   基数排序   |       O(n*k)       |       O(n*k)       |       O(n*k)       |     O(n+k)     | Out-place    |    稳定    |
|   计数排序   |       O(n+k)       |       O(n+k)       |       O(n+k)       |      O(k)      | Out-place    |    稳定    |

图片名词解释：

- n:数据规模
- k:“桶的个数”
- In-place:占用常数内存，不用额外占用内存
- Out-palce:占用额外内存

### 术语说明

- 稳定：如果a原本在b前面，而a=b，排序之后a仍然在b的前面；
- 不稳定：如果a原本在b的前面，而a=b，排序之后a可能会出现在b的后面；
- 内排序：所有排序操作都在内存中完成；
- 外排序：由于数据太大，因此把数据放在磁盘中，而排序通过磁盘和内存的数据传输才能进行；
- 时间复杂度： 一个算法执行所耗费的时间。
- 空间复杂度：运行完一个程序所需内存的大小。



## 一、冒泡排序(BubbleSort)

冒泡排序是一种简单的排序算法。它重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。 

### 算法描述

1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
3. 针对所有的元素重复以上的步骤，除了最后一个；
4. 重复步骤1~3，直到排序完成。

### 动图演示

![avatar]()

### 代码实现

```python
def bubble_sort(blist):
    endPoint = length = len(blist)
    for i in range(length):
        flag = True
        for j in range(1, endPoint):
            if blist[j - 1] > blist[j]:
                blist[j - 1], blist[j] = blist[j], blist[j - 1]
                endPoint = j
                flag = False
        if flag:
            break
    return blist
```



## 二、选择排序(SelectionSort)

选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

### 算法描述 

n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果。具体算法描述如下：

1. 初始状态：无序区为R[1..n]，有序区为空；
2. 第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
3. n-1趟结束，数组有序化了。

### 动图演示

![](.\algorithm-sort-summary\images\SelectionSort.gif)

### 代码实现

```python
def select_sort(slist):
    for i in range(len(slist)):
        minPoint = i
        for j in range(i, len(slist)):
            if slist[j] < slist[minPoint]:
                minPoint = j
        slist[i], slist[minPoint] = slist[minPoint], slist[i]
    return slist
```



## 三、插入排序(InsertSort)

插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

### 算法描述

一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：

1. 从第一个元素开始，该元素可以认为已经被排序；
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5. 将新元素插入到该位置后；
6. 重复步骤2~5。

### 动图演示

![](C:\Users\F1333239\Desktop\2018-10-17\algorithm-sort-summary\images\InsertSort.gif)

### 代码实现

```python
def insert_sort(ilist):
    for i in range(len(ilist)):
        for j in range(i):
            if ilist[i] < ilist[j]:
                ilist.insert(j, ilist.pop(i))
                break
    return ilist
```



## 四、希尔排序(ShellSort)

1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫**缩小增量排序**。

### 算法描述

先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：

1. 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
2. 按增量序列个数k，对序列进行k 趟排序；
3. 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

### 动图演示

![](C:\Users\F1333239\Desktop\2018-10-17\algorithm-sort-summary\images\ShellSort.gif)

### 代码实现

```python
def shell_sort(slist):
    length = len(slist)
    gap = round(length / 2) 
    while gap > 0:
        for i in range(gap, length):  
            temp = slist[i]
            j = i
            while j >= gap and slist[j - gap] > temp:  
                slist[j] = slist[j - gap]
                j -= gap
            slist[j] = temp
        gap = round(gap / 2)  
    return slist
```



## 五、归并排序(MergeSort)

归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。 

### 算法描述

1. 把长度为n的输入序列分成两个长度为n/2的子序列；
2. 对这两个子序列分别采用归并排序；
3. 将两个排序好的子序列合并成一个最终的排序序列。

### 动图演示

![](C:\Users\F1333239\Desktop\2018-10-17\algorithm-sort-summary\images\MergeSort.gif)

### 代码实现

```python
def merge_sort(mlist):
    if len(mlist) <= 1:
        return mlist
    mid = int(len(mlist) / 2) 
    left = merge_sort(mlist[:mid])
    right = merge_sort(mlist[mid:])
    return merge(left, right) 

def merge(left, right):
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
```



## 六、快速排序(QuickSort)

快速排序的基本思想：通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序。

### 算法描述

快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：

1. 从数列中挑出一个元素，称为 “基准”（pivot）；
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

### 动图演示

![](C:\Users\F1333239\Desktop\2018-10-17\algorithm-sort-summary\images\QuickSort.gif)

### 代码实现

```python
def quick_sort(qlist):
    return qsort(qlist, 0, len(qlist) - 1)

def qsort(qlist, left, right):
    if left >= right:
        return qlist
    key = qlist[left]  
    lp = left
    rp = right
    while lp < rp:
        while qlist[rp] >= key and lp < rp:
            rp -= 1
        while qlist[lp] <= key and lp < rp:
            lp += 1
        qlist[lp], qlist[rp] = qlist[rp], qlist[lp]
    qlist[left], qlist[lp] = qlist[lp], qlist[left]
    qsort(qlist, left, lp - 1)
    qsort(qlist, rp + 1, right)
    return qlist
```



## 七、堆排序(HeapSort)

堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。

### 算法描述

1. 将初始待排序关键字序列(R1,R2….Rn)构建成大顶堆，此堆为初始的无序区；
2. 将堆顶元素R[1]与最后一个元素R[n]交换，此时得到新的无序区(R1,R2,……Rn-1)和新的有序区(Rn),且满足R[1,2…n-1]<=R[n]；
3. 由于交换后新的堆顶R[1]可能违反堆的性质，因此需要对当前无序区(R1,R2,……Rn-1)调整为新堆，然后再次将R[1]与无序区最后一个元素交换，得到新的无序区(R1,R2….Rn-2)和新的有序区(Rn-1,Rn)。不断重复此过程直到有序区的元素个数为n-1，则整个排序过程完成。

### 动图演示

![](C:\Users\F1333239\Desktop\2018-10-17\algorithm-sort-summary\images\HeapSort.gif)

### 代码实现

```python
def heap_sort(hlist):
    length = len(hlist)
    first = int(length / 2 - 1) 
    for start in range(first, -1, -1):  
        max_heapify(hlist, start, length - 1)
    for end in range(length - 1, 0, -1):  
        hlist[end], hlist[0] = hlist[0], hlist[end]
        max_heapify(hlist, 0, end - 1)
    return hlist

def max_heapify(hlist, start, end):
    root = start
    while True:
        child = root * 2 + 1  
        if child > end:
            break
        if child + 1 <= end and hlist[child] < hlist[child + 1]:
            child += 1  
        if hlist[root] < hlist[child]: 
            hlist[root], hlist[child] = hlist[child], hlist[root]
            root = child
        else:
            break
```



## 八、基数排序(RadixSort)

基数排序也是非比较的排序算法，对每一位进行排序，从最低位开始排序，复杂度为O(kn),为数组长度，k为数组中的数的最大的位数；

基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。基数排序基于分别排序，分别收集，所以是稳定的。

### 算法描述

1. 取得数组中的最大数，并取得位数；
2. array为原始数组，从最低位开始取每个位组成radix数组；
3. 对radix进行计数排序（利用计数排序适用于小范围数的特点）。

### 动图演示

![](C:\Users\F1333239\Desktop\2018-10-17\algorithm-sort-summary\images\RadixSort.gif)

### 代码实现

```python
def radix_sort(rlist, radix=10):
    length = len(rlist)
    if rlist is None or length < 2:
        return rlist
    maxValue = max(rlist)
    maxDigit = 0
    while maxValue != 0:
        maxValue //= 10 
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
```



## 九、计数排序(CountingSort)

计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。

### 算法描述

1. 找出待排序的数组中最大和最小的元素；
2. 统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
3. 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
4. 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。

### 动图演示

![](C:\Users\F1333239\Desktop\2018-10-17\algorithm-sort-summary\images\CountingSort.gif)

### 代码实现

```python
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
```



## 十、桶排序(BucketSort)

桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）

### 算法描述

1. 设置一个定量的数组当作空桶；
2. 遍历输入数据，并且把数据一个一个放到对应的桶里去；
3. 对每个不是空的桶进行排序；
4. 从不是空的桶里把排好序的数据拼接起来。 

### 图片演示

![](C:\Users\F1333239\Desktop\2018-10-17\algorithm-sort-summary\images\BucketSort.png)

### 代码实现

```python
def bucket_sort(blist, bucketSize=5):
    length = len(blist)
    if length == 0:
        return blist
    minValue = maxValue = blist[0]
    for i in range(length):
        if blist[i] < minValue:
            minValue = blist[i]
        elif blist[i] > maxValue:
            maxValue = blist[i]
    bucketCount = int((maxValue - minValue) / bucketSize) + 1
    buckets = []
    for i in range(bucketCount):
        buckets.append([])
    for i in range(length):
        buckets[int((blist[i] - minValue) / bucketSize)].append(blist[i])
    sort_list = []
    for i in range(bucketCount):
        insert_sort(buckets[i])
        for j in range(len(buckets[i])):
            sort_list.append(buckets[i][j])
    return sort_list
```

