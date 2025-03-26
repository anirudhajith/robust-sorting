import sort.base as base

class QuickSort(base.Sort):
    def partition(self, arr, low, high):
        i = low - 1
        pivot = arr[high]

        for j in range(low, high):
            if self.compare(arr[j], pivot) <= 0:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def sort(self, arr):
        def _sort(arr, low, high):
            if low < high:
                pi = self.partition(arr, low, high)

                _sort(arr, low, pi - 1)
                _sort(arr, pi + 1, high)

        _sort(arr, 0, len(arr) - 1)
        return arr