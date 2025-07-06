#Joanna Faye P. Manio (sorted-descending)
import heapq

class Minheap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def get_min(self):
        return self.heap[0] if self.heap else None

    def remove_min(self):
        return heapq.heappop(self.heap) if self.heap else None
#for sort
    def heap_sort(self):
        sorted_list = []
        while self.heap:
            sorted_list.append(self.remove_min())
        return sorted_list

    def heapify(self, array):
        heapq.heapify(array)
        self.heap = array

    def display_heap(self):
        return self.heap

def main_min_heap():
    min_heap = Minheap()
    array = [10, 20, -30, 50, 60, 5]

    #ilagay ng element
    for num in array:
        min_heap.insert(num)

    print(f'Heap Elements: {min_heap.display_heap()}')

    #Sort in ascending Order and maprint
    sorted_array = min_heap.heap_sort()
    print(f'Sorted Array (Ascending): {sorted_array}')

if __name__ == '__main__':
    main_min_heap()
