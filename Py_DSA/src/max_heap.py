#JOANNA FAYE P. MANIO BS CPE 2A
import heapq
#negate value = =-value
# self = -self
#heapq.heappop = -heapq.heappop
class Maxheap:
    def __init__(self): #constructor
        self.heap = []#constructor

    def insert(self, value):
        heapq.heappush(self.heap, -value)#negate the value "-value" kasi walang maxheap ung python

    def get_max(self):
        return -self.heap[0] if self.heap else None #if there is value in the heap, get the index 0 or min element. return none if nothing

    def remove_max(self):
        return -heapq.heappop(self.heap) if self.heap else None #if there is value it will pop. if no value, none
#negate mga elenets sa  [] self.heap
    def display_heap(self):# you cant display the full tree but in python, u can
        return [-x for x in self.heap]

def main() -> None:
    max_heap = Maxheap()
    max_heap.insert(10)
    max_heap.insert(20)
    max_heap.insert(-30)
    print(f'Max Element: {max_heap.get_max()}')
    print(f'Remove Max Element: {max_heap.remove_max()}')#peek
    print(f'New Max Element: {max_heap.get_max()}')
    print(f'All Element: {max_heap.display_heap()}')#display all display_heap

#value -> negate to insert -> negate it back(double negate it will be the same value)

if __name__ == '__main__':
    main()
