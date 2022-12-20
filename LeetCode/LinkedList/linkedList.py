class Node:
    next = None

    def __init__(self, val) -> None:
        self.val = val

    def __repr__(self) -> str:
        return(f'{self.val} -> {self.next}')

def countNodes(head):
    count = 1

    current = head

    while current.next is not None:
        current = current.next

        count += 1
    return count

def middleOfLinkedList(head):
    current = [head]

    while current[-1].next is not None:
        current.append(current[-1].next)


    return  current[len(current)//2]

def middleOfLinkedListPointers(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)




# print(head)
print(middleOfLinkedList(head))
print("pointers", middleOfLinkedListPointers(head))