import math


sampleList = [4,7,2,6,1,4,7,3,5,2]

def merge_sort(list, listBegin, listEnd):
    if listBegin < listEnd:
            endListPartition = math.floor((listBegin + listEnd)/2)
            merge_sort(list, listBegin, endListPartition)
            merge_sort(list, endListPartition+1, listEnd)
            merge(list, listBegin, endListPartition, listEnd)

def merge(list, listBegin, endListPartition, listEnd):
    subList1Length = endListPartition - listBegin + 1
    subList2Length = listEnd - endListPartition
    subList1 = [None] * subList1Length
    subList2 = [None] * subList2Length

    i = 0
    while i < subList1Length:
        subList1[i] = list[listBegin + i-1]
        i = i+1
    
    j = 0
    while j < subList2Length:
        subList2[j] = list[endListPartition + j]
        j = j + 1

    subList1[subList1Length] = float('inf')
    subList2[subList2Length] = float('inf')


    i = 0
    j = 0

    k = 0
    while k < listEnd:  
        if subList1[i] <= subList2[j]:
            list[k] = subList1[i]
            i = i+1
        else: 
            list[k] = subList2[j]
            j = j+1


print("SampleList unsorted:")
print(sampleList)

merge_sort(sampleList, 1, 11)
print("SampleList sorted:")
print(sampleList)
