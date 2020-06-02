'''
二分法查找
O(nlogn)
'''
def binarysearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2 #向下取整
        guess = list[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

list = [1,2,3,4,5,6,7,8]
print(binarysearch(list, 3))


'''
选择排序
O(n^2)
需要建立新表
'''
def SearchSort(list):
    newarr = []
    for i in range(len(list)):
        a = list.index(min(list))
        newarr.append(list.pop(a))
    return newarr
list = [1,7,3,5,4,6,16,8,2,14]
print(SearchSort(list))


'''
冒泡排序
O(n^2)
'''
def BubbleSort(list):
    while 1:
        state = 0
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i+1], list[i] = list[i], list[i+1]
                state = 1
            else:
                continue

        if state == 0: #没有发生交换时停止
            break
        else:
            continue
    return list
list = [1,7,3,5,4,6,16,8,2,14]
print(BubbleSort(list))


'''
插入排序
O(n^2)
'''
def InsertionSort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]  #符合while条件，j+1 = i位置进行空出，然后进行后移一位
            j -= 1

        list[j + 1] = key #最后将key插入当前空位
    return list

list = [1,7,3,5,4,6,16,8,2,14]
print(InsertionSort(list))
