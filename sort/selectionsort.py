import sort.base as base

class SelectionSort(base.Sort):
    def sort(self, arr):
        for i in range(len(arr)):
            min_index = i
            for j in range(i + 1, len(arr)):
                if self.compare(arr[j], arr[min_index]) < 0:
                    min_index = j
            arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr
    