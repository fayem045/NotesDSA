from collections import deque

class CustomDoublyCircular:
    def __init__(self):#constructor
        self.list = deque()

    #insert at LAst
    def append(self,value):
        self.list.append(value)#the data

    #insert at beginning
    def prepend(self, value):
        self.list.appendleft(value)

        #remove at beginning
    def remove_beginning(self):
        if self.list:
            self.list.popleft()#pop if meron
        else:
            print("list is empty")

        #Remove at end
    def remove_end(self):
        if self.list:
            self.list.pop()
        else:
            print('List is empty')

    def display(self):
        if not self.list:
            print('list is empty')
        else:
            for i in range(len(self.list)):#kukunin length ng self list
                print(self.list[i], end = "<->")#every print may <->
            print(self.list[0]) #PRINT PINAKA UNA

def main() -> None:
    dll = CustomDoublyCircular()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(4)#naginsert uli, doble ya(circular)
    dll.display()
    dll.remove_beginning()
    dll.remove_end()
    dll.display()#2- 1 kasi bumalik sa front ng list circular kasi
    dll.remove_beginning()
    dll.display()

if __name__ == '__main__':
    main()