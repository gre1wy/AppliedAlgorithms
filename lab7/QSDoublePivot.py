import sys
import time
class QuickSortDoublePivot:
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
            leftpivot, rightpivot = self.partition(arr, low, high)
            self.memory_used += sys.getsizeof(leftpivot)
            self.memory_used += sys.getsizeof(rightpivot)
            self.sort_runner(arr, low, leftpivot - 1)
            self.sort_runner(arr, leftpivot + 1, rightpivot - 1)
            self.sort_runner(arr, rightpivot + 1, high)

    def partition(self, arr, low, high):
        self.comparisons += 1
        if arr[low] > arr[high]:
            self.swaps += 1
            arr[low], arr[high] = arr[high], arr[low]
        
        pivot1 = arr[low]
        pivot2 = arr[high]

        self.memory_used += sys.getsizeof(pivot1)    
        self.memory_used += sys.getsizeof(pivot2)

        i = low + 1
        lt = low + 1
        gt = high - 1

        self.memory_used += sys.getsizeof(lt)
        self.memory_used += sys.getsizeof(lt)
        self.memory_used += sys.getsizeof(i)

        while i <= gt:
            self.comparisons += 1
            if arr[i] < pivot1:
                self.comparisons += 1
                self.swaps += 1
                arr[i], arr[lt] = arr[lt], arr[i]
                lt += 1
            elif arr[i] > pivot2:
                self.comparisons += 1
                self.swaps += 1
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
                i -= 1
            i += 1

        self.swaps += 1
        arr[low], arr[lt - 1] = arr[lt - 1], arr[low]
        self.swaps += 1
        arr[high], arr[gt + 1] = arr[gt + 1], arr[high]

        return lt - 1, gt + 1
