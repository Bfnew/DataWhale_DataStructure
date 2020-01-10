# -*- coding:utf-8 -*-
"""
@author: Xiaoxin
@file: task2_linkList.py
@time: 2020/1/5 23:22
"""

"定义链表"
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    """
    目的：合并两个有序链表

    思路：遍历l1和l2，取其小者作为下一个节点；取两个指针，一个作为初始赋值指针，一个用于新增新的值
    """
    def mergeTwoLists(self, l1, l2):
        ans = tmp = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                tmp.next, l1 = l1, l1.next
            else:
                tmp.next, l2 = l2, l2.next
            tmp = tmp.next
        tmp.next = l1 or l2
        return ans.next


class Solution2:
    """
    目的：给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

    思路：使用快慢指针，一个指针比另一个指针快n个节点，
    """
    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head
        for i in range(n):
            if fast.next:
                fast = fast.next
            else:
                "防止该链表没有n个节点，则返回头节点"
                return head.next

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


class Solution3:
    """
    目的：给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

    思路：先把链表首尾相连，再找到位置断开循环 或将尾部向前数第K个元素作为头，原来的头接到原来的尾上
    """
    def rotateRight(self, head, k):
        "首先排除极端情况"
        if head is None or head.next is None: return head
        start, end, i = head, None, 0
        while head:
            i += 1
            end = head
            head = head.next
        #构成圆
        end.next = start
        pos = i - k % i
        while pos > 1:
            start = start.next
            pos -= 1
        res = start.next
        start.next = None
        return res



from pythonds import *

a = [1, 3, 5, 2, 9]

b = Stack()
for i in a:
    b.push(i)

c = Queue()
for i in a:
    c.enqueue(i)

print(b.items)
print(c.items)