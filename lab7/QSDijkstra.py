import sys
import time
import random
class QuickSortDijkstra:
    def __init__(self):
        self.swaps = 0
        self.comparisons = 0
        self.exec_time = 0
        self.memory_used = 0

    def clean_metrics(self):
        self.swaps = 0
        self.comparisons = 0
        self.exec_time = 0
        self.memory_used = 0

    def show_metrics(self):
        print(f"Swaps: {self.swaps}")
        print(f"Comparisons: {self.comparisons}")
        print(f"Execution time: {self.exec_time} seconds")
        print(f"Memory used: {self.memory_used//1024} KB")
        
    def qsort(self, arr):
        self.clean_metrics()
        start_time = time.time()
        self.sort_runner(arr, 0, len(arr) - 1)
        self.exec_time = time.time() - start_time

    def sort_runner(self, arr, low, high):
        if low < high:
            lt, gt = self.partition(arr, low, high)
            self.memory_used += sys.getsizeof(lt)
            self.memory_used += sys.getsizeof(gt)
            self.sort_runner(arr, low, lt - 1)
            self.sort_runner(arr, gt + 1, high)

    def partition(self, arr, low, high):
        pivot_index = self.median_of_three_random(arr, low, high)
        pivot = arr[pivot_index]
        arr[pivot_index], arr[low] = arr[low], arr[pivot_index]  
        self.swaps += 1

        lt = low  
        gt = high  
        i = low + 1  
        self.memory_used += sys.getsizeof(lt)
        self.memory_used += sys.getsizeof(lt)
        self.memory_used += sys.getsizeof(i)
        while i <= gt:
            if arr[i] < pivot:
                self.comparisons += 1
                self.swaps += 1
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
                self.comparisons += 1
                self.swaps += 1
                arr[gt], arr[i] = arr[i], arr[gt]
                gt -= 1
            else:
                i += 1

        return lt, gt

    def median_of_three_random(self, arr, low, high):
        range_size = high - low + 1
        if range_size < 3:
            return high
        indices = random.sample(range(low, high + 1), 3)
        a, b, c = indices[0], indices[1], indices[2]

        self.comparisons += 3
        if arr[b] < arr[a]:
            self.swaps += 1
            a, b = b, a
        if arr[c] < arr[a]:
            self.swaps += 1
            a, c = c, a

        if arr[c] < arr[b]:
            self.swaps += 1
            b, c = c, b
        return b

