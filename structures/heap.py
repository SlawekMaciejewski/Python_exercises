import random
from heapq import heappush, heappop

def heapsort(iterable):
    heap = []
    for value in iterable:
        heappush(heap, value)
    return [heappop(heap) for i in range(len(heap))]

if __name__ == '__main__':
    random_list = random.sample(range(100), 10)
    print(random_list)
    sorted_list = heapsort(random_list)
    print(sorted_list)
