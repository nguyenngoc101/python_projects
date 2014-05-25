def binarySearch(key, array, first, last):
    pivot = (first + last)/2
    if first > last:
        return -1
    if key == array[pivot]:
        return pivot
    if key > array[pivot]:
       return binarySearch(key, array, pivot+1, last)
    if key < array[pivot]:
       return binarySearch(key, array, first, pivot-1)

def search(key, array):
    first = 0
    last = len(array) - 1
    while first <= last:
        mid = (first + last)/2
        if key==array[mid]:
            return mid
        if key < array[mid]:
            last = mid - 1
        if key > array[mid]:
            first = mid + 1

    return -1



if __name__=="__main__":
    #print binarySearch(0, [0,1,2,3,4,5,7,8,9,11,15,16], 0, 11)
    #print binarySearch(1, [1], 0, 1)
    print search(1, [0,1])
    sum = 1.00000000000000
    for x in range(1,5):
        sum *= 1.0000000000000/x
        print "%s" % 1/x
    print sum
