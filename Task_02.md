



# Task02 顺序表和链表

## 1. 线性表的定义与操作

**1.1 线性表的定义**

线性表（Linear List）是由`n（n >= 0）`个相同类型的数据元素`a1,a2,...,an` 组成的有序序列。即表中除首尾元素外，其它元素有且仅有一个直接前驱和直接后继。首元素仅有一个直接后继，尾元素仅有一个直接前驱。表中数据元素的个数称为表的长度，记为：`(a1,a2,...,an)`。


**1.2 线性表的操作**
- 随机存取：获取或设置指定索引处的数据元素值。（支持索引器）
- 插入操作：将数据元素值插入到指定索引处。
- 移除操作：移除线性表指定索引处的数据元素。
- 查找操作：寻找具有特征值域的结点并返回其下标。
- 得到表长：获取线性表中实际包含数据元素的个数。
- 是否为空：判断线性表中是否包含数据元素。
- 清空操作：移除线性表中的所有数据元素。

![线性表接口](https://img-blog.csdnimg.cn/20191219081504351.png)

---
## 2. 线性表的存储与实现

**2.1 顺序存储（顺序表）**

定义：利用顺序存储结构（即利用数组）实现的线性表。

特点：逻辑结构与存储结构相同；具有随机存取的特点。

![顺序表存储示意图](https://img-blog.csdnimg.cn/20191219081751681.png)

实现：

![利用顺序存储结构实现线性表](https://img-blog.csdnimg.cn/20191219082422397.png)


**2.2 链式存储（链表）**

利用指针方式实现的线性表称为链表（单链表、循环链表、双链表）。它不要求逻辑上相邻的数据元素在物理位置上也相邻，即：逻辑结构与物理结构可以相同也可以不相同。

**2.2.1 单链表**

定义：每个结点只含有一个链域（指针域）的链表。即：利用单链域的方式存储线性表的逻辑结构。

结构：

![单链表存储结构](https://img-blog.csdnimg.cn/201912190831277.png)

实现：

对结点的封装：

![对单链表结点的封装](https://img-blog.csdnimg.cn/20191219083410202.png)


对单链表的封装：

![对单链表的封装](https://img-blog.csdnimg.cn/20191219084222597.png)





**2.2.2 循环链表**

定义：是一种首尾相连的单链表。即：在单链表中，将尾结点的指针域null改为指向pHead，就得到单链形式的循环链表。

表现形式：

![利用头指针表示循环链表](https://img-blog.csdnimg.cn/20191219084644144.png)

通常情况下，使用尾指针表示循环链表。

![利用尾指针表示循环链表](https://img-blog.csdnimg.cn/20191219084747468.png)

实现：

![对循环链表的封装](https://img-blog.csdnimg.cn/20191219084946540.png)




**2.2.3 双链表**

定义：每个结点含有两个链域（指针域）的链表。即：利用双链域的方式存储线性表的逻辑结构。

结构：

![双链表存储结构](https://img-blog.csdnimg.cn/20191219085239419.png)

实现：

对结点的封装：

![对双链表结点的封装](https://img-blog.csdnimg.cn/20191219085534618.png)



对双链表的封装：

![对双向链表的封装](https://img-blog.csdnimg.cn/2019121909023162.png)



---
## 3. 练习参考答案

**1. 合并两个有序链表**

以下代码为`Python`版本：

```python
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

```




**2. 删除链表的倒数第N个节点**

 以下代码为`Python`版本：

```python
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

```



**3. 旋转链表**(将其构造成循环链表来处理了)

以下代码为`Python`版本：

```Python
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

```
