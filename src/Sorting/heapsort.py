
__about__ = """

HEAP SORT ALGORITHM IMPLEMENTATION

"""

"""
MAX HEAP SOLUTION.
"""

def BuildMaxHeap(array,size,i):

    left = 2*i +1
    right= 2*i +2
    largest = i
    if left < size and array[left] > array[largest]:
        largest = left
    if right < size and array[largest] < array[right]:
        largest = right

    if largest != i:
        array[largest], array[i] = array[i], array[largest]

        BuildMaxHeap(array, size, largest)

def heapsort(arr):

    for i in range(0,len(arr)):
        BuildMaxHeap(arr,len(arr),i)

    for j in range(len(arr) - 1, 0, -1):
        arr[j], arr[0] = arr[0], arr[j]  # swap
        BuildMaxHeap(arr, j, 0)


if __name__ == "__main__":
    # Driver code to test above
    arr = [12, 11, 13, 5, 6, 7]
    heapsort(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d" % arr[i]),
        # This code is contributed by Mohit Kumra



