def quick_sort_first(a):
    if len(a) < 2:
        return a
    else:
        pivot = a[0]
        less = [i for i in a[1:] if i <= pivot]
        greater = [i for i in a[1:] if i > pivot]
        b = quick_sort_first(less) + [pivot] + quick_sort_first(greater)
        a[:] = b[:]
        return a


a = [5, 4, 3, 2, 1]
print(quick_sort_first(a))
quick_sort_first(a)
print(a)
