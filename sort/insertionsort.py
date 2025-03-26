import sort.base as base

class InsertionSort(base.Sort):
    def sort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and self.compare(arr[j], key) > 0:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr