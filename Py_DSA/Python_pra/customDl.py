from collections import deque

class customDl:
    def __init__(self):
        self.list = deque()

    def append(self,value):
        self.list.append(value)

    def prepend(self,value):
        if self.list:
            self.list.appendleft(value)
        else:
            self.list.append(value)

    def insertAtIndex(self,index,value):
        if index < 0:
            return
        if index == 0:
            self.list.appendleft(value)
        elif index >= len(self.list):
            self.list.append(value)
        else:
            temp_list = list(self.list)
            temp_list.insert(index,value)
            self.list = deque(temp_list)

    def display(self):
            if not self.list:
                print('list is empty')
            else:
                for i in range(len(self.list)):
                    print(self.list[i], end = " <-> ")
                print("null")

def main() -> None:
    myTreasuure = customDl()
    myTreasuure.append(1)
    myTreasuure.display()
    myTreasuure.prepend(2)
    myTreasuure.display()
    myTreasuure.insertAtIndex(3,5)
    myTreasuure.display()

if __name__ == '__main__':
    main()




