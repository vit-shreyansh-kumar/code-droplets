
__about__ = """

Quick Sort Algorithm

"""


def partition(array, low, high):

    i = low -1
    pivot = array[high]
    if low < high:

        for j in range(low,high):

            if array[j] <= pivot:
                i = i+1
                array[i],array[j] = array[j],array[i]

        array[i+1], array[high] = array[high],array[i+1]

    return i+1


def QuickSort(array, low, high):

    if low < high:

        #Partition Point Index
        # partition_index i.e pivot is now at the right place
        partition_index = partition(array, low, high)

        # Since pivot is placed at the right place so we dont need to utilize it now we just need to sort before and after it.
        #i.e partition_index - 1 hence we again begin with partition_index +1

        QuickSort(array, low, partition_index-1)
        QuickSort(array, partition_index+1, high)


if __name__ == "__main__":

    array = [50, 23, 67, 33, 1, 22, 99, 101, 55, 26, 59, 91, 108, 104, 87]
    len = len(array)
    QuickSort(array,0,len-1)

    print("==================QUICK SORT===================")
    print("======== TIME COMPLEXITY: O(n log n)===========")
    print(array)
    print("===============================================")

