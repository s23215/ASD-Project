import sys
import time

def mergeSort(tab):
    if len(tab) > 1:
        mid = len(tab) // 2
        L = tab[:mid]
        R = tab[mid:]
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                tab[k] = L[i]
                i += 1
            else:
                tab[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            tab[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            tab[k] = R[j]
            j += 1
            k += 1
def mergeSortShow(tab):
    start_time = time.time()
    sys.setrecursionlimit(1000000000)

    # tab = [16,4,14,10,7,2,6,11,50,10]*100000000
    mergeSort(tab)
    # print(tab)

    print("MergeSort: %s sekund" % (time.time() - start_time))
