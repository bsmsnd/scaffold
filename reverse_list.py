from typing import Optional
from type_define import ListNode

def plus(x, y):
    return x + y
    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        p1 = head
        p2 = head.next
        p1.next = None
        while (p2 is not None):
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        return p1
        
#var=
result = plus(1, 2)
print("This is the sum: 1, 2, %s" % result)