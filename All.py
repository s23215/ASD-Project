import random

import CountingSort
import HeapSort
import MergeSort
import QucikSort

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

randomTab = [0]* 1000000
for i in range(0,len(randomTab)):
    randomTab[i]=random.randint(1,10000)

print("For random:")
HeapSort.heapSortShow(randomTab)
CountingSort.countingSortShow(randomTab)
MergeSort.mergeSortShow(randomTab)
QucikSort.qucikSortShow(randomTab)

mergeSort(randomTab)

print("For Sorted")
HeapSort.heapSortShow(randomTab)
CountingSort.countingSortShow(randomTab)
MergeSort.mergeSortShow(randomTab)
QucikSort.qucikSortShow(randomTab)

randomTab.reverse()

print("For Reverse Sorted")
HeapSort.heapSortShow(randomTab)
CountingSort.countingSortShow(randomTab)
MergeSort.mergeSortShow(randomTab)
QucikSort.qucikSortShow(randomTab)