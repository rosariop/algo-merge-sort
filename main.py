import math

#sampleList = [4,7,2,6,1,4,7,3,5,2]
sampleList = [4,7,6,2]

def merge_sort(listA, listBegin, listEnd):
    if listBegin < listEnd:
            endListPartition = math.floor((listBegin + listEnd)/2)
            merge_sort(listA, listBegin, endListPartition)
            merge_sort(listA, endListPartition + 1, listEnd)
            merge(listA, listBegin, endListPartition, listEnd)

def merge(listA, listBegin, endListPartition, listEnd):
    subList1Length = endListPartition - listBegin + 1
    subList2Length = listEnd - endListPartition
    subList1 = []
    subList2 = []

    i = 0
    while i < subList1Length:
        subList1.append(listA[listBegin + i])
        i = i+1
    
    j = 0
    while j < subList2Length:
        subList2.append(listA[endListPartition + j + 1])
        j = j + 1

    subList1.append(float('inf'))
    subList2.append(float('inf'))


    i = 0
    j = 0
    print(listA)
    k = listBegin
    while k < listEnd:  
        if subList1[i] <= subList2[j]:
            listA[k] = subList1[i]
            i = i+1
        else: 
            listA[k] = subList2[j]
            j = j+1
        k = k + 1
        
    print(listA)

print("SampleList unsorted:")
print(sampleList)

merge_sort(sampleList, 0, 3)
print("SampleList sorted:")
print(sampleList)