# def max_heapify(arr, n, i):
#     largest = i  # Initialize largest as root
#     l = 2 * i + 1  # left = 2*i + 1
#     r = 2 * i + 2  # right = 2*i + 2

#     # If left child is larger than root
#     if l < n and arr[l] > arr[largest]:
#         largest = l

#     # If right child is larger than largest so far
#     if r < n and arr[r] > arr[largest]:
#         largest = r

#     # Change root, if needed
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]  # Swap
#         # Recursively heapify the affected sub-tree
#         max_heapify(arr, n, largest)

# def build_max_heap(arr):
#     n = len(arr)
#     # Build a maxheap
#     for i in range(n // 2 - 1, -1, -1):
#         max_heapify(arr, n, i)

# arr = [3, 8, 2, 5, 1, 4, 7, 6]
# build_max_heap(arr)
# print(arr)

def bucket_sort(arr):
    # 創建十個桶子
    n = len(arr)
    buckets = [[] for _ in range(10)]
    
    # 將元素放入桶子中
    for num in arr:
        index = int(num * 10)
        buckets[index].append(num)
    
    # 對每個桶子內的元素進行排序（這裡使用插入排序）
    for bucket in buckets:
        bucket.sort()
    
    # 合併各個桶子內的元素
    result = []
    for bucket in buckets:
        result.extend(bucket)
    
    return result, [len(bucket) for bucket in buckets]

# 輸入的浮點數陣列
arr = [0.03, 0.28, 0.67, 0.10, 0.78, 0.52, 0.43, 0.49, 0.94, 0.15]

# 使用桶子排序法進行排序並計算每個桶子內的元素個數
sorted_arr, bucket_sizes = bucket_sort(arr)
print("排序後的陣列:", sorted_arr)
print("每個桶子內的元素個數:", bucket_sizes)


