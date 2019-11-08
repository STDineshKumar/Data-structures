#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1_root = ListNode(1)
temp = l1_root
for i in range(2, 10):
    while(temp.next is not None):
        temp = temp.next
    temp.next = ListNode(i)
 
print(temp)
temp = l1_root
while(temp.next is not None):
    print(temp.val)
    temp=temp.next

print(l1_root)
print("--------")
l2_root = ListNode(4)
temp = l2_root
for i in range(5, 15):
    while(temp.next is not None):
        temp = temp.next
    temp.next = ListNode(i)

temp = l2_root
while(temp.next is not None):
    print(temp.val)
    temp = temp.next

# Merge twolist with out creating new nodes.
def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    root_l2, root_l1 = l2, l1
    temp_l2, temp_l1 = l2, l1
    result = ListNode(0)
    result_head = result
    while(root_l1.next is not None and root_l2.next is not None):
        root_l1 = root_l1.next
        root_l2 = root_l2.next
        if temp_l1.val <= temp_l2.val:
                result.next = temp_l1
                result = result.next
                result.next = temp_l2
                result = result.next
                
        elif temp_l1.val > temp_l2.val:
                result.next = temp_l2
                result = result.next
                result.next = temp_l1
                result = result.next
        temp_l1 = temp_l1.next
        temp_l2 = temp_l2.next

    if (root_l1.next is not None and root_l2.next is None):
            result.next = temp_l2
    
    elif (root_l1.next is None and root_l2.next is not None):
            result.next = temp_l1

    return result_head.next

temp = mergeTwoLists(l1_root, l2_root)
while(temp.next is not None):
     print(temp.val)
     temp = temp.next
