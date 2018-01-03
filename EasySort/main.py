import datetime


def BubbleSort(a):
    n = len(a)
    ok = 1
    while ok:
        ok = 0
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                a[i + 1], a[i] = a[i], a[i + 1]
                ok = 1
    return a


def BubbleSortOp(a):
    n = len(a)
    ok = 1
    while ok:
        ok = 0
        for i in range(0, n - 1):
            if a[i] > a[i + 1]:
                a[i + 1], a[i] = a[i], a[i + 1]
                ok = 1
        n -= 1
    return a


def inter(left, right):
    i = 0
    j = 0
    list = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            list.append(left[i])
            i += 1
        else:
            list.append(right[j])
            j += 1
    while i < len(left):
        list.append(left[i])
        i += 1
    while j < len(right):
        list.append(right[j])
        j += 1

    return list


def merge(a):
    if len(a) > 1:
        m = len(a) // 2
        left = a[:m]
        right = a[m:]
        left = merge(left)
        right = merge(right)
        a = inter(left, right)
    return a


a = [list(range(40000, 0, -1))]
t1 = datetime.datetime.now()
a = merge(a)
t2 = datetime.datetime.now()
print(t2 - t1)
k = [list(range(40000, 0, -1))]
t1 = datetime.datetime.now()
k.sort()
t2 = datetime.datetime.now()
print(t2 - t1)
