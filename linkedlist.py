class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        self.add_item_at_n(0,data)

    def delete(self, data):
        if self.head == None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head

        while current_node.next != None and current_node.next.data != data:
            current_node = current_node.next
        if current_node.next != None:
            current_node.next = current_node.next.next
    
    def print_list(self):
        current_node = self.head
        while current_node != None:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("End")
    
    def length(self):
        current_length = 0
        if self.head == None:
            return current_length
        current_node = self.head
        current_length += 1
        while current_node.next != None:
            current_length += 1
            current_node = current_node.next
        return current_length
    
    def reverse(self):
        if self.head.next == None:
            return
        current_node = self.head
        prev_node = None
        next_node = None
        for i in range(0,self.length()):
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def return_nth_term(self,term:int):
        count = 0
        current_node = self.head
        if not term > self.length()-1:
            while count != term:
                count += 1
                current_node = current_node.next

            return current_node.data
        return

    def add_item_at_n(self,location,data):
        if not location > self.length():
            count = 0
            new_node = Node(data)
            if not location == 0:
                count += 1
                current_node = self.head
                while count != location:
                    current_node = current_node.next
                    count += 1
                new_next = current_node.next
                current_node.next = new_node
                new_node.next = new_next
            else:
                new_node.next = self.head
                self.head = new_node

    def sort_list(self):
        for j in range(self.length()-1):
            current_node = self.head
            prev_node = None
            next_node = None
            for i in range(self.length()-2):
                next_node = current_node.next
                if current_node.data > next_node.data:
                    temp_node = next_node.next
                    next_node.next = current_node
                    current_node.next = temp_node
                    if prev_node == None:
                        self.head = next_node
                    else:
                        prev_node.next = next_node
                    prev_node = next_node
                else:
                    prev_node = current_node
                    current_node = current_node.next
    def merge_list(self,list):
        current_node = list.head
        for i in range(list.length()):
            self.append(current_node.data)
            current_node = current_node.next
        self.sort_list()
        
# Example usage
if __name__ == "__main__":
    ll = linkedList()
    ll.append(5)
    ll.append(4)
    ll.append(6)
    ll.append(2)


    kk = linkedList()
    kk.append(3)
    kk.append(7)
    kk.append(8)
    kk.append(1)
    kk.append(9)

    ll.merge_list(kk)
    print("Original List:")
    ll.print_list()



        