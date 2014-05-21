def bubbleSort(array):
    size = len(array)
    for i in range(size-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print "bubble sort: %s " % array

def selectionSort(array):
    size = len(array)
    for i in range(size):
        for j in range(i+1, size):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
    print "selectionSort: %s " % array

def insertionSort(array):
    size = len(array)
    for i in range(1, size):
        for j in range(i-1, -1, -1):
            if array[i] < array[j]:
                temp = array[i]
                for k in range(i-1, j-1, -1):
                    array[k+1] = array[k]
                array[j] = temp

    print "insertionSort: %s" % array

if __name__=="__main__":
    arr = [9,8,7,6,5,8,3,2,1,0]
    arr = [0,1,2,3,4,5,6,7,8,8,9]
    bubbleSort(arr)
    selectionSort(arr)
    insertionSort(arr)
