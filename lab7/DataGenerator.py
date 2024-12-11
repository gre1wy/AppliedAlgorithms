import random
def identical(size, value = 1):
        return [value] * size

def sorted(size):
    return list(range(size))

def random_data(size, low=0, high=1000):
    return [random.randint(low, high) for _ in range(size)]

def almost_sorted(size, swap_percentage=5):
    arr = list(range(size))
    swaps = max(1, (swap_percentage * size) // 100)
    print(swaps)
    for _ in range(swaps):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def reverse_order(size):
    return list(range(size, 0, -1))

def triangular(size):
    half = size // 2
    first_half = list(range(half))
    second_half = first_half[::-1]
    return first_half + second_half