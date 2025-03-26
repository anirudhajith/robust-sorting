import sort.base as base

class HeapSort(base.Sort):
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and self.compare(arr[i], arr[l]) < 0:
            largest = l

        if r < n and self.compare(arr[largest], arr[r]) < 0:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

    def sort(self, arr):
        n = len(arr)

        for i in range(n, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

        return arr