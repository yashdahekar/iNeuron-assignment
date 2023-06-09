print("Que no 1. ==> ")
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def create_new_linked_list(list1, list2):
    dummy_node = Node()  
    current = dummy_node

    while list1 is not None and list2 is not None:
        if list1.data >= list2.data:
            new_node = Node(list1.data)
            list1 = list1.next
        else:
            new_node = Node(list2.data)
            list2 = list2.next
        current.next = new_node
        current = new_node

    while list1 is not None:
        new_node = Node(list1.data)
        current.next = new_node
        current = new_node
        list1 = list1.next

    while list2 is not None:
        new_node = Node(list2.data)
        current.next = new_node
        current = new_node
        list2 = list2.next

    return dummy_node.next  
list1 = Node(5)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(8)

list2 = Node(1)
list2.next = Node(7)
list2.next.next = Node(4)
list2.next.next.next = Node(5)

result = create_new_linked_list(list1, list2)

while result is not None:
    print(result.data, end="->")
    result = result.next

print("Que no 2. ==> ")
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def remove_duplicates(head):
    current = head

    while current is not None and current.next is not None:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head
head = Node(11)
head.next = Node(11)
head.next.next = Node(11)
head.next.next.next = Node(21)
head.next.next.next.next = Node(43)
head.next.next.next.next.next = Node(43)
head.next.next.next.next.next.next = Node(60)

result = remove_duplicates(head)

while result is not None:
    print(result.data, end="->")
    result = result.next

print("Que no 3. ==> ")
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_k_nodes(head, k):
    current = head
    next = None
    prev = None
    count = 0

    while current is not None and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    if next is not None:
        head.next = reverse_k_nodes(next, k)

    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)

k = 4

result = reverse_k_nodes(head, k)

while result is not None:
    print(result.data, end=" ")
    result = result.next

print("Que no 4. ==> ")

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse_alternate_k_nodes(head, k):
    current = head
    prev = None
    next = None
    count = 0

    while current is not None and count < k:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1

    count = 0
    while current is not None and count < k:
        prev = current
        current = current.next
        count += 1

    if current is not None:
        prev.next = reverse_alternate_k_nodes(current, k)

    return prev

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)

k = 3

result = reverse_alternate_k_nodes(head, k)

while result is not None:
    print(result.data, end="->")
    result = result.next

print("Que no 5. ==> ")

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def delete_last_occurrence(head, key):
    prev = None
    current = head
    last_occurrence_prev = None
    last_occurrence = None

    while current is not None:
        if current.data == key:
            last_occurrence_prev = prev
            last_occurrence = current

        prev = current
        current = current.next

    if last_occurrence is None:
        return head

    if last_occurrence_prev is None:
        head = head.next
    else:
        last_occurrence_prev.next = last_occurrence.next

    return head

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(5)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(10)

key = 2

result = delete_last_occurrence(head, key)

while result is not None:
    print(result.data, end="->")
    result = result.next

print("Que no 6. ==> ")

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def merge_sorted_lists(a, b):
    dummy = Node()
    current = dummy

    while a is not None and b is not None:
        if a.data <= b.data:
            current.next = a
            a = a.next
        else:
            current.next = b
            b = b.next
        current = current.next

    if a is not None:
        current.next = a
    else:
        current.next = b

    return dummy.next

a = Node(5)
a.next = Node(10)
a.next.next = Node(15)

b = Node(2)
b.next = Node(3)
b.next.next = Node(20)

result = merge_sorted_lists(a, b)

while result is not None:
    print(result.data, end="->")
    result = result.next

a = Node(1)
a.next = Node(1)

b = Node(2)
b.next = Node(4)

result = merge_sorted_lists(a, b)

while result is not None:
    print(result.data, end="->")
    result = result.next
    
print("Que no 7. ==> ")

class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def reverse_doubly_linked_list(head):
    current = head
    temp = None

    while current is not None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        current = current.prev

    if temp is not None:
        head = temp.prev

    return head

head = Node(10)
head.next = Node(8)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next
head.next.next.next = Node(2)
head.next.next.next.prev = head.next.next

result = reverse_doubly_linked_list(head)

while result is not None:
    print(result.data, end=" ")
    result = result.next

print("Que no 8. ==> ")

class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def delete_node_at_position(head, position):
    if position == 1:
        if head is not None:
            head = head.next
            if head is not None:
                head.prev = None
        return head

    current = head
    count = 1

    while current is not None and count < position:
        current = current.next
        count += 1

    if current is None:
        return head

    current.prev.next = current.next

    if current.next is not None:
        current.next.prev = current.prev

    current.prev = None
    current.next = None

    return head

head = Node(1)
head.next = Node(3)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next

position = 3

result = delete_node_at_position(head, position)

while result is not None:
    print(result.data, end=" ")
    result = result.next
