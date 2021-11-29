import sys
import time

def countingSort(tab,tab1,n):
    x = [0] * 10001
    for i in range(0, n):
        x[tab[i]] += 1

    for i in range(1, 51):
        x[i] += x[i - 1]

    i = n - 1
    while i >= 0:
        tab1[x[tab[i]] - 1] = tab[i]
        x[tab[i]] -= 1
        i -= 1

    for i in range(0, n):
        tab[i] = tab1[i]
def countingSortShow(tab):
    start_time = time.time()
    sys.setrecursionlimit(1000000000)

    # tab = [16,4,14,10,7,2,6,11,50,10]*100000000
    n = len(tab)
    tab1 = [0] * n

    countingSort(tab,tab1,n)
    # print(tab)

    print("Counting Sort: %s sekund" % (time.time() - start_time))
