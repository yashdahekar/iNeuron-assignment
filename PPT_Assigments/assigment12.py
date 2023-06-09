print("Que no. 1 ==> ")
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle_node(head):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    prev = None

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        prev = slow
        slow = slow.next

    prev.next = slow.next

    return head
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

result = delete_middle_node(head)

while result is not None:
    print(result.val, end=" ")
    result = result.next

print("Que no. 2 ==> ")
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_loop(head):
    if head is None or head.next is None:
        return False

    tortoise = head
    hare = head.next

    while hare is not None and hare.next is not None:
        if tortoise == hare:
            return True

        tortoise = tortoise.next
        hare = hare.next.next

    return False
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = head.next
result = has_loop(head)
print(result)

print("Que no. 3 ==> ")
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_nth_from_end(head, n):
    if head is None:
        return None

    main_ptr = head
    ref_ptr = head

    count = 0
    while count < n:
        if ref_ptr is None:
            return None  
        ref_ptr = ref_ptr.next
        count += 1
    while ref_ptr is not None:
        main_ptr = main_ptr.next
        ref_ptr = ref_ptr.next

    return main_ptr.val
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)

result = find_nth_from_end(head, 2)

print(result)

print("Que no. 4 ==> ")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head):
    if head is None or head.next is None:
        return True
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    second_half = reverse(slow.next)
    slow.next = None  
    first_half = head

    while first_half is not None and second_half is not None:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True

def reverse(head):
    prev = None
    curr = head

    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    return prev
head1 = ListNode('R')
head1.next = ListNode('A')
head1.next.next = ListNode('D')
head1.next.next.next = ListNode('A')
head1.next.next.next.next = ListNode('R')

result1 = is_palindrome(head1)
print(result1)  

print("Que no. 5 ==> ")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_loop(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or fast.next is None:
        return head

    slow = head

    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None

    return head

head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = head.next
result = remove_loop(head)
while result is not None:
    print(result.val, end=" ")
    result = result.next

print("Que no. 6 ==> ")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def skip_delete(head, M, N):
    if head is None or M <= 0 or N <= 0:
        return head

    current = head
    count = 1

    while current is not None:
        while count < M and current.next is not None:
            current = current.next
            count += 1

        if current is None:
            break

        temp = current.next
        for _ in range(N):
            if temp is None:
                break
            temp = temp.next

        current.next = temp
        current = temp
        count = 0

    return head
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(3)
head1.next.next.next = ListNode(4)
head1.next.next.next.next = ListNode(5)
head1.next.next.next.next.next = ListNode(6)
head1.next.next.next.next.next.next = ListNode(7)
head1.next.next.next.next.next.next.next = ListNode(8)
result1 = skip_delete(head1, 2, 2)
current = result1
while current is not None:
    print(current.val, end=" ")
    current = current.next
print()

print("Que no. 7 ==> ")
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_lists(first, second):
    if first is None:
        return second
    if second is None:
        return first
    while first is not None and second is not None:
        temp = second
        second = second.next
        temp.next = first.next
        first.next = temp
        first = temp.next

    return first
first_head = ListNode(5)
first_head.next = ListNode(7)
first_head.next.next = ListNode(17)
first_head.next.next.next = ListNode(13)
first_head.next.next.next.next = ListNode(11)

second_head = ListNode(12)
second_head.next = ListNode(10)
second_head.next.next = ListNode(2)
second_head.next.next.next = ListNode(4)
second_head.next.next.next.next = ListNode(6)


result_head = merge_lists(first_head, second_head)


current = result_head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")

current = second_head
while current is not None:
    print(current.val, end=" -> ")
    current = current.next
print("None")

print("Que no. 8 ==> ")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_circular(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next

    return False
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = head

result = is_circular(head)

print(result)
