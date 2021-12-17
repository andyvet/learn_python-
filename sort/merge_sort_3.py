def merge_3(a, b, d):
    i = k = j = n = 0
    c = [None] * (len(a) + len(b) + len(d))
    while i < len(a) and k < len(b) and j < len(d):
        if a[i] <= b[k] and a[i] <= d[j]:
            c[n] = a[i]
            n += 1
            i += 1
        elif  b[k] < a[i] and b[k] < d[j]:
            c[n] = b[k]
            n += 1
            k += 1
        else:
            c[n] = d[j]
            n += 1
            j += 1
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            n += 1
            i += 1
        else:
            c[n] = b[k]
            n += 1
            k += 1
    while i < len(a) and j < len(d):
        if a[i] <= d[j]:
            c[n] = a[i]
            n += 1
            i += 1
        else:
            c[n] = d[j]
            n += 1
            j += 1
    while k < len(b) and j < len(d):
        if b[k] <= d[j]:
            c[n] = b[k]
            n += 1
            k += 1
        else:
            c[n] = d[j]
            n += 1
            j += 1
    while i < len(a):
        c[n] = a[i]
        n += 1
        i += 1
    while k < len(b):
        c[n] = b[k]
        n += 1
        k += 1
    while j < len(d):
        c[n] = d[j]
        n += 1
        j += 1
    return c


def merge_sort_3(a):
    if len(a) <= 1:
        return
    middle_1 = len(a) // 3
    middle_2 = 2 * middle_1 + 1
    L = a[:middle_1]
    M = a[middle_1:middle_2]
    R = a[middle_2:]
    merge_sort_3(L)
    merge_sort_3(M)
    merge_sort_3(R)
    c = merge_3(L, M, R)
    a[:] = c[:]
    return

a = [5, 4, 3, 10, 11, 58, 34, 67, 1, 28, 59, 41, 98, 24, 38, 62, 78, 13, 19, 20, 30, 95]
merge_sort_3(a)
print(a)