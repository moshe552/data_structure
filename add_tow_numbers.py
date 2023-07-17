# Definition for singly-linked list.
from typing import Optional
from linked_link import LinkedList


def add_toe_numbers(l_1: Optional[LinkedList], l_2: Optional[LinkedList]) -> Optional[LinkedList]:
    """
    The function will sum the numbers that represent by the given lists
    (most significant digit is the first in list) and return it as list.
    :param l_1: the first number that represent by the list.
    :param l_2: the second number that represent by the list.
    :return: A list that represents the sum.
    """
    num_1 = 0
    num_2 = 0
    res_lst = LinkedList()
    if l_1.head.value == 0 and l_2.head.value == 0:
        res_lst.append(0)
        return res_lst
    current_node = l_1.head
    while current_node is not None:
        num_1 = (num_1 * 10) + current_node.value
        current_node = current_node.next
    current_node = l_2.head
    while current_node is not None:
        num_2 = (num_2 * 10) + current_node.value
        current_node = current_node.next
    res = num_1 + num_2
    while res > 0:
        res_lst.add_first(res % 10)
        res = res // 10
    return res_lst


l1 = LinkedList()
l2 = LinkedList()
l1.append(0)
l1.append(2)
l1.append(4)
l1.append(3)
l2.append(0)
l2.append(6)
l2.append(4)
res_list = add_toe_numbers(l1, l2)
res_list.print_linked_list()

l1 = LinkedList()

