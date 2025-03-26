import sort.base as base

class BubbleSort(base.Sort):
    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.compare(arr[j], arr[j+1]) > 0:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr