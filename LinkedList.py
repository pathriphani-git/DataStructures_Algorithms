class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class Linkedlist():
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head == None:
            self.head=Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def print(self):
        if self.head == None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_values(self,datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def get_length(self):
        count=0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index to remove from List")
        if index == 0:
            self.head = self.head.next
            return
        count=0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at_index(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index to Insert")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count=0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count += 1

    def insert_after_value(self,data_after,data_to_insert):
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next)
                break
            itr = itr.next

    def remove_by_value(self,data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == '__main__':
    ll = Linkedlist()
    ll.insert_values(["Mango","Banana","Peach"])
    ll.print()
    ll.remove_by_value("Mango")
    ll.print()
    ll.remove_by_value("Peach")
    ll.print()
    ll.remove_by_value("Banana")
    ll.print()


