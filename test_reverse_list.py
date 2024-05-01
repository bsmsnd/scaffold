from type_define import ListNode
from reverse_list import plus
from reverse_list import Solution

def test_add():
    assert plus(1, 2) == 3


def test_reverse_list():
    p3 = ListNode(3)
    p2 = ListNode(2, p3)
    p1 = ListNode(1, p2)
    sol = Solution()
    p_result = sol.reverseList(p1)
    assert p_result.val == 3
    assert p_result.next.val == 2
    assert p_result.next.next.val == 1
    assert p_result.next.next.next == None
