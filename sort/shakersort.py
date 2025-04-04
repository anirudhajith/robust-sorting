import sort.base as base

class ShakerSort(base.Sort):
    def sort(self, arr):
        n = len(arr)
        swapped = True
        start = 0
        end = n - 1

        while swapped:
            swapped = False

            for i in range(start, end):
                if self.compare(arr[i], arr[i + 1]) > 0:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            if not swapped:
                break

            swapped = False
            end -= 1

            for i in range(end - 1, start - 1, -1):
                if self.compare(arr[i], arr[i + 1]) > 0:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
                    swapped = True

            start += 1

        return arr