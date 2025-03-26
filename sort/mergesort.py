import sort.base as base

class MergeSort(base.Sort):
    def merge(self, arr, l, m, r):
        n1 = m - l + 1
        n2 = r - m

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[l + i]

        for i in range(n2):
            R[i] = arr[m + 1 + i]

        i = 0
        j = 0
        k = l

        while i < n1 and j < n2:
            if self.compare(L[i], R[j]) <= 0:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def sort(self, arr):
        if len(arr) > 1:
            m = len(arr) // 2
            L = arr[:m]
            R = arr[m:]

            self.sort(L)
            self.sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if self.compare(L[i], R[j]) <= 0:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        return arr