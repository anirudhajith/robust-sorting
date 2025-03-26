import copy

from comparator.base import Comparator
from sort.bubblesort import BubbleSort
from sort.heapsort import HeapSort
from sort.insertionsort import InsertionSort
from sort.mergesort import MergeSort
from sort.selectionsort import SelectionSort
from sort.shakersort import ShakerSort
from sort.shellsort import ShellSort
from sort.quicksort import QuickSort

def sort(arr, algorithm: str, comparator: Comparator):
    """
    Sorts an array using the specified algorithm.
    
    :param arr: The array to sort.
    :param comparator: The comparator function to use.
    :param algorithm: The algorithm to use.
    :return: The sorted array.
    """

    arr = copy.deepcopy(arr)
    if algorithm == 'bubblesort':
        return BubbleSort(comparator).sort(arr)
    elif algorithm == 'heapsort':
        return HeapSort(comparator).sort(arr)
    elif algorithm == 'insertionsort':
        return InsertionSort(comparator).sort(arr)
    elif algorithm == 'mergesort':
        return MergeSort(comparator).sort(arr)
    elif algorithm == 'selectionsort':
        return SelectionSort(comparator).sort(arr)
    elif algorithm == 'shakersort':
        return ShakerSort(comparator).sort(arr)
    elif algorithm == 'shellsort':
        return ShellSort(comparator).sort(arr)
    elif algorithm == 'quicksort':
        return QuickSort(comparator).sort(arr)
    else:
        raise ValueError("Invalid algorithm")
