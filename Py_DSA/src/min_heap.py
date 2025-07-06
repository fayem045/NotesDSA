#JOANNA FAYE P. MANIO BS CPE 2A(unsorted)
import heapq

class Minheap:
    def __init__(self): #constructor
        self.heap = []#constructor

    def insert(self, value):
        heapq.heappush(self.heap, value)

    def get_min(self):
        return self.heap[0] if self.heap else None #if there is value in the heap, get the index 0 or min element. return none if nothing

    def remove_min(self):
        return heapq.heappop(self.heap) if self.heap else None #if there is value it will pop. if no value, none

    def display_heap(self):# you cant display the full tree but in python, u can
        return self.heap

def main() -> None:
    min_heap = Minheap()
    min_heap.insert(10)
    min_heap.insert(20)
    min_heap.insert(-30)
    print(f'Min Element: {min_heap.get_min()}')
    print(f'Remove Min Element: {min_heap.remove_min()}')#peek
    print(f'Display New Min: {min_heap.get_min()}')
    print(f'All Element: {min_heap.display_heap()}')#display all display_heap


if __name__ == '__main__':
    main()
