from timeit import Timer
from random import *
import time

def bubbleSort(array):
    size = len(array)
    for i in range(size-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def selectionSort(array):
    size = len(array)
    for i in range(size):
        for j in range(i+1, size):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]

def selectionSort2(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
              positionOfMax = location
              temp = alist[fillslot]
              alist[fillslot] = alist[positionOfMax]
              alist[positionOfMax] = temp


def insertionSort(array):
    size = len(array)
    for i in range(1, size):
        for j in range(i-1, -1, -1):
            if array[i] < array[j]:
                temp = array[i]
                for k in range(i-1, j-1, -1):
                    array[k+1] = array[k]
                array[j] = temp


def insertionSort2(array):
    size = len(array)
    for i in range(1, size):
        tmp = array[i]
        k = i
        while k > 0 and array[k] < array[k-1]:
            array[k-1], array[k] = array[k], array[k-1]
            k -= 1

def mergeSort(array, first, last):
    if first < last:
        mid = (first + last)/2
        mergeSort(array, first, mid)
        mergeSort(array, mid+1, last)
        mix(array, first, mid+1, last)
    return array

def mix(array, first, mid, last):
    size = last - first + 1
    temp = [0]*size
    for i in range(0, size):
        temp[i] = array[first+i]
    i = first
    j = mid
    for k in range(0,size):
        if i == mid:
           array[first+k] = temp[j-first]
           j += 1
           continue
        if j == (last+1):
           array[first+k] = temp[i-first]
           i += 1
           continue

        if temp[i-first] > temp[j-first]:
           array[first+k] = temp[j-first]
           j += 1
        else:
           array[first+k] = temp[i-first]
           i += 1

def benchMark(func):
    def func_decorator(*args, **kwargs):
        start = time.time()
        arr = func(*args, **kwargs)
        end = time.time()
        print "%s: %s" % (func.__name__, end - start)
        return arr

    return func_decorator

def mergeSort2(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort2(lefthalf)
        mergeSort2(righthalf)
        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
                k=k+1
        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

    return alist

def quickSort(array, first, last):
    if first < last:
        pivot = partition(array, first, last)
        quickSort(array, first, pivot-1)
        quickSort(array, pivot+1, last)

def partition(array, first, last):
    pivot = (first + last)/2
    return position

if __name__=="__main__":
    arr = [0]*1000
    for x in range(1000):
        arr[x] = randint(0,100)
    print "initializing...................................."
    first = 0
    last = len(arr) - 1
    #bubble = benchMark(bubbleSort)
    #selection = benchMark(selectionSort)
    #selection2 = benchMark(selectionSort2)
    #insertion = benchMark(insertionSort)
    #insertion2 = benchMark(insertionSort2)
    merge = benchMark(mergeSort)
    merge2 = benchMark(mergeSort2)
    #bubble(arr)
    #selection(arr)
    #selection2(arr)
    #insertion(arr)
    #insertion2(arr)
    print merge(arr,first,last)
    print merge2(arr)
    #t1 = Timer(" bubbleSort(arr)", "from __main__ import bubbleSort")
    #print("bubbleSort ",t1.timeit(number=1000), "milliseconds")
