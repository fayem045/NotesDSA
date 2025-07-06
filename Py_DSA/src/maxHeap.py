#Joanna Faye P Manio (sorted-Descending)
import heapq

class Maxheap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, -value)  # Insert negative para mabaliktad/negate

    def get_max(self):
        return -self.heap[0] if self.heap else None

    def remove_max(self):
        return -heapq.heappop(self.heap) if self.heap else None

    def heap_sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.remove_max())
        return sorted_list

    def heapify(self, array):
        self.heap = [-x for x in array]
        heapq.heapify(self.heap)

    def display_heap(self):
        return [-x for x in self.heap]

def main_max_heap():
    max_heap = Maxheap()
    array = [10, 20, -30, 50, 60, 5]

    # Insert elements sa heap
    for num in array:
        max_heap.insert(num)

    print(f'Heap Elements: {max_heap.display_heap()}')

    # Heap Sort for descending tapos print
    sorted_array = max_heap.heap_sort()
    print(f'Sorted Array (Descending): {sorted_array}')

if __name__ == '__main__':
    main_max_heap()
