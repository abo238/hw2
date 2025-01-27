import math

def insertion_sort_steps(n):
    return 8 * n**2

def merge_sort_steps(n):
    return 64 * n * math.log2(n)

n = 1
while insertion_sort_steps(n) <= merge_sort_steps(n):
    n += 1

print(f"Минимальное значение n, при котором сортировка вставкой медленнее: {n}")