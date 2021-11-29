import sys
import time

def heapify(tab, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and tab[i] < tab[l]:
        largest = l

    if r < n and tab[largest] < tab[r]:
        largest = r

    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]

        heapify(tab, n, largest)

def heapSort(tab):
    n = len(tab)

    for i in range(n // 2 - 1, -1, -1):
        heapify(tab, n, i)

    for i in range(n - 1, 0, -1):
        tab[i], tab[0] = tab[0], tab[i]
        heapify(tab, i, 0)

def heapSortShow(tab):
    start_time = time.time()
    sys.setrecursionlimit(1000000000)

    # tab = [16,4,14,10,7,2,6,11,50,10]*10000000
    heapSort(tab)
    # print(tab)

    print("HeapSort: %s sekund" % (time.time() - start_time))