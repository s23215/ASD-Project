import time
import sys

def partition(tab, low, high):
    i = (low - 1)
    r = tab[high]

    for j in range(low, high):
        if tab[j] <= r:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]

    tab[i + 1], tab[high] = tab[high], tab[i + 1]
    return (i + 1)

def quickSort(tab, low, high):
    if len(tab) == 1:
        return tab
    if low < high:
        q = partition(tab, low, high)

        quickSort(tab, low, q - 1)
        quickSort(tab, q + 1, high)

def qucikSortShow(tab):
    start_time = time.time()
    sys.setrecursionlimit(1000000000)

    # tab = [16,4,14,10,7,2,6,11,50,10]*1000
    n = len(tab)
    quickSort(tab, 0, n - 1)

    # print (tab)
    print("QuickSort: %s sekund" % (time.time() - start_time))