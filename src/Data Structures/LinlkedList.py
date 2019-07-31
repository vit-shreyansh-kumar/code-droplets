
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert_node(self,value):
        if self.head is None:
            self.head = Node(value)
            self.curr = self.head

        else:
            temp = Node(value)
            self.curr.next = temp
            self.curr = temp

    def print_list(self):

        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete_node(self,data):

        temp = self.head
        while temp:

            if temp.next.data == data:
                temp.next = temp.next.next

            temp = temp.next


if __name__ == "__main__":

    ll = LinkedList()
    ll.insert_node(1)
    ll.insert_node(2)
    ll.insert_node(3)
    ll.insert_node(4)
    ll.insert_node(5)
    ll.insert_node(6)
    ll.insert_node(7)
    ll.insert_node(8)

    ll.delete_node(5)

    ll.print_list()
