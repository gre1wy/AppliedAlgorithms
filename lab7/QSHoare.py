import sys
import time
import random

class QuickSortHoare:
    def __init__(self, pivot_type):
        self.pivot_type = pivot_type
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
            p = self.partition(arr, low, high)
            self.memory_used += sys.getsizeof(p)
            self.sort_runner(arr, low, p)
            self.sort_runner(arr, p + 1, high)

    def partition(self, arr, low, high):
        pivot_index = self.pivot_selector(arr, low, high)
        self.memory_used += sys.getsizeof(pivot_index)

        pivot = arr[pivot_index]
        self.memory_used += sys.getsizeof(pivot)

        arr[pivot_index], arr[low] = arr[low], arr[pivot_index]
        self.swaps += 1

        left = low - 1
        right = high + 1
        self.memory_used += sys.getsizeof(left)
        self.memory_used += sys.getsizeof(right)

        while True:
            left += 1
            self.comparisons += 1
            while arr[left] < pivot:
                self.comparisons += 1
                left += 1

            right -= 1
            self.comparisons += 1
            while arr[right] > pivot:
                self.comparisons += 1
                right -= 1

            self.comparisons += 1
            if left >= right:
                return right

            arr[left], arr[right] = arr[right], arr[left]
            self.swaps += 1

    def pivot_selector(self, arr, low, high):
        if self.pivot_type == "last":
            return high
        elif self.pivot_type == "random":
            return random.randint(low, high)
        elif self.pivot_type == "median_of_three":
            return self.median_of_three(arr, low, high)
        elif self.pivot_type == "median_of_three_random":
            return self.median_of_three_random(arr, low, high)
        else:
            raise ValueError(f"Invalid pivot type: {self.pivot_type}")

    def median_of_three(self, arr, low, high):
        mid = (low + high) // 2
        self.comparisons += 3
        if arr[low] > arr[mid]:
            self.swaps += 1
            low, mid = mid, low
        if arr[low] > arr[high]:
            self.swaps += 1
            low, high = high, low
        if arr[mid] > arr[high]:
            self.swaps += 1
            mid, high = high, mid
        return mid

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
