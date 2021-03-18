# 数据结构与算法

数据结构（data structure）是计算机存储、组织数据的方式。数据结构是指相互之间存在一种或者多种特定关系的数据元素的集合。

算法（Algorithm）是指解题方案的准确而完整的描述，是一系列解决问题的清晰指令，算法代表着用系统的方法描述解决问题的策略机制。

程序是一组计算机能够识别和执行的指令，可以简单的理解为程序 = 数据结构 + 算法

**为什么学习数据结构？**

数据结构所表现的是：如何对现实问题进行建模，并且采用合适的算法高效解决问题。这是一种计算思维，与语言无关，与工具无关，它是我们从现实世界走向计算机世界的桥梁。

## 常用的数据结构

### 1. 栈

栈（stack）又名堆栈，它是一种运算受限的线性表。其限制是仅允许在表的一端进行插入和删除运算。

![栈](.\static\img\stack.png)

栈允许进行插入和删除操作的一端称为栈顶(top)，另一端称为栈底（bottom）；栈底固定，而栈顶浮动；栈中元素个数为零时称为空栈。插入一般称为进栈（push），删除则称为退栈（pop）。

由于堆叠数据结构只允许在一端进行操作，因而按照后进先出（LIFO，Last In First Out）的原理运作。栈也称为后进先出表。

**复杂度分析**：

栈属于常见的一种线性结构，对于进栈和退栈而言，时间复杂度都为O(1)。

**主要代码实现：**

```python
class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, element):
        """进栈，向栈压入一个元素"""
        if len(self.stack) >= self.limit:
            raise StackOverflowException("Stack Overflow Exception")
        else:
            self.stack.append(element)

    def pop(self):
        """退栈，从栈中弹出一个元素"""
        if self.stack:
            self.stack.pop()
        else:
            raise StackEmptyException("Stack Empty Exception")
```

**其他功能实现：**

```python
def is_empty(self):
    """判断栈是否为空"""
    return not bool(self.stack)

def peek(self):
    """查看栈顶元素"""
    if self.stack:
        return self.stack[-1]
    else:
        return None

def size(self):
    """查看栈的大小"""
    return len(self.stack)

def clear(self):
    """清空栈中的元素"""
    self.stack = []
```

**完整代码：**

[数据结构-栈](./Stack.py)

**栈的应用：**

![栈的应用](.\static\img\{A0096DD1-8162-486B-B4FE-F904C726835D}_20200423152344.jpg)

**括号匹配：**

> **有效括号字符串**需满足：
>
> - 左括号必须用相同类型的右括号闭合。
> - 左括号必须以正确的顺序闭合。
> - 注意空字符串可被认为是有效字符串。
>
> **举例：**
>
> ((())): True
>
> ((()): False
>
> (())): False
>
> **目标：**
>
> 1. 使用一个堆栈作为数据结构
> 2. 来检查括号字符串是否完全匹配

**主要代码实现：**

```python
def balanced_parentheses(parentheses):
    limit = len(parentheses)
    stack = Stack(limit=limit)
    for i in parentheses:
        if i == '(':
            # 如果是左括号则进栈
            stack.push(i)
        elif i == ')':
            # 如果是右括号则退栈
            if not stack.is_empty():
                stack.pop()
            else:
                return False
    else:
        return True
```

**完整代码：**[栈的应用-括号匹配](.\exercises\balanced_parentheses.py)

**算法思想：**

判断一个表达式的”(“和”）”是否匹配，思路是这样的：遇到”（“则入栈，遇到”）”则从栈顶弹出”（“与之配成一对，当整个表达式扫描完毕时：

（1） 若栈内为空，则说明（与）是匹配的。

（2） 若表达式扫描完毕，栈内仍有（则说明左括号是多的。

（3） 若当）被扫描到，栈里却没有（能弹出了，说明）多，表达式中）也是多的。

### 2. 链表

在看链表之前，先了解下什么是线性表。

**线性表：0个或多个数据元素的有限序列**

线性表的两种存储结构：**顺序存储结构和链式存储结构**

顺序存储结构：用一段地址**连续**的存储单元依次存储线性表的数据元素

链式存储结构：地址**可以连续**也可以**不连续**的存储单元存储数据元素

![线性表](.\static\img\0e2442a7d933c8957e627c16bef188f4830200a2.jpeg)

![顺序结构与链式结构的对比](.\static\img\3bf33a87e950352a57ee4dd925a100f6b0118bbf.jpeg)

**链表：**（linked list）是物理存储单元上非连续的、非顺序的存储结构，数据元素的逻辑顺序是通过链表的指针地址实现，每个元素包含两个结点，一个是存储元素的数据域（内存空间），另一个是指向下一个结点地址的指针域。

根据指针的指向，链表能形成不同的结构，例如单链表、双向链表、循环链表等。

![链式存储结构](.\static\img\f11f3a292df5e0fe42a2ef293382cfac5fdf7243.jpeg)

链表通过将链点i与其邻居链点i+1通过指针相关联，从索引0到索引N-1对链点进行排序。

#### 2.1 单链表

**主要代码实现：**

```python
class Linked_List:
    def __init__(self, head=None):
        """
        链表初始化函数
        """
        self.head = head  # 表示链表的头部元素

    def append(self, new_element):
        """
        向链表添加新的结点
        """
        # 将头部结点指向临时变量current
        current = self.head
        # 当头部结点存在时
        if self.head:
            # 循环到链表的最后一个元素
            while current.next:
                current = current.next
            current.next = new_element
        # 当头部结点不存在时
        else:
            self.head = new_element

    def insert(self, position, new_element):
        """
        在链表中指定索引处插入元素
        """
        if position < 0 or position > self.get_length():
            raise IndexError("When insert new element, out of the index limit")
        temp = self.head
        # 将插入元素的next属性指向老的头结点，并将新的元素赋值给头结点
        if position == 0:
            new_element.next, self.head = temp, new_element
            return
        i = 0
        # 遍历找到索引值为position的结点后，在其后面插入结点
        while i < position:
            pre, temp = temp, temp.next
            i += 1
        pre.next, new_element.next = new_element, temp

    def remove(self, position):
        """
        删除指定索引的链表元素
        """
        if position < 0 or position > self.get_length() - 1:
            raise IndexError(
                'Out of the index limit on delete the element')
        i = 0
        temp = self.head
        # 当存在链表元素时才能执行删除操作
        while temp is not None:
            # 将头结点的后一个结点赋值给新的头结点，再将之前的头结点指向None
            if position == 0:
                self.head = temp.next
                temp.next = None
                return True
            # 以此来遍历列表
            pre, temp = temp, temp.next
            i += 1
            if i == position:
                # 将pre的next属性指向temp的下一个结点
                pre.next, temp.next = temp.next, None
                return
```

**其他功能实现：**

```python
    def print_list(self):
        """
        遍历链表，并将元素依次打印出来
        """
        print("linked list:")
        # 将头部结点赋值给临时变量temp
        temp = self.head
        new_list = []
        while temp is not None:
            new_list.append(temp.data)
            temp = temp.next
        print(new_list)

    def reverse(self):
        """
        将列表反转
        """
        prev = None
        current = self.head
        while current:
            next_node, current.next = current.next, prev
            prev, current = current, next_node
        self.head = prev

    def initlist(self, data_list):
        """
        将列表转换为链表
        """
        # 创建头结点
        self.head = Node(data_list[0])
        temp = self.head
        # 逐个为data中的数据创建结点，建立链表
        for i in data_list[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def is_empty(self):
        """
        判断链表是否为空
        """
        return not self.head

    def get_length(self):
        """
        获取链表的长度
        """
        # 将头部结点赋值给临时结点
        temp = self.head
        # 计算链表的长度变量
        length = 0
        while temp is not None:
            length = length + 1
            temp = temp.next
        # 返回链表的长度
        return length
```



**完整代码：**

[数据结构-单链表](.\linked_list.py)

**复杂度分析：**

链表属于常见的一种线性结构，对于插入和移除而言，时间复杂度都为O(1)。

但是对于搜索操作而言，不管从链表的头部还是尾部，都需要遍历O(n)，所以最好复杂度为O(1)，最坏的情况就是从头部遍历到尾部才搜索出对应的元素，所以最坏复杂度为O(n)，平均复杂度为O(n)。

归纳如下：

- 最好复杂度为 O(1)
- 最坏复杂度为 O(n)
- 平均复杂度为 O(n)