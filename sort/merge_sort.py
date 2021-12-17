def merge(a, b):
    i = k = n = 0
    c = [None] * (len(a) + len(b))
    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            n += 1
            i += 1
        else:
            c[n] = b[k]
            n += 1
            k += 1
    while i < len(a):
        c[n] = a[i]
        n += 1
        i += 1
    while k < len(b):
        c[n] = b[k]
        n += 1
        k += 1
    return c


def merge_sort(a):
    if len(a) <= 1:
        return
    middle = len(a) // 2
    L = a[:middle]
    R = a[middle:]
    merge_sort(L)
    merge_sort(R)
    c = merge(L, R)
    a[:] = c[:]
    return


a = [5, 4, 3, 2, 1]
merge_sort(a)
print(a)