class Node:
    def __init__(self, value=None, next=None):
        self._value = value  # 元素值
        self._next = next    # 下一节点链点

    def get_value(self):
        """获取节点的值"""
        return self._value

    def get_next(self):
        """获取下一节点的链点"""
        return self._next

    def set_value(self, new_value):
        """设置节点的值"""
        self._value = new_value

    def set_next(self, new_next):
        """设置节点下一节点的链点"""
        self._next = new_next


class LinkedList:
    def __init__(self):
        self._head = Node()
        # self._tail = None
        # self._length = 0

    def is_empty(self):
        """查看链表是否为空"""
        return self._head == None

    def size(self):
        """查看链表的大小"""
        current = self._head
        length = 0
        while current != None:
            length += 1
            current = current.get_next()
        return length

    def add(self, value):
        """在链表的头部添加节点"""
        new_node = Node(value, None)
        new_node.set_next(self._head)
        self._head = new_node

    def append(self, value):
        """在链表的尾部追加节点"""
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(new_node)

    def insert(self, position, value):
        """在链表的任意位置插入节点"""
        if position <= 1:
            self.add(value)
        elif position > self.size():
            self.append(value)
        else:
            temp = Node(value)
            count = 1
            pre = None
            current = self._head
            while count < position:
                count += 1
                pre = current
                current = current.get_next()
                pre.set_next(temp)
                temp.set_next(current)

    def search(self, value):
        """查询链表是否存在某个节点"""
        current = self._head
        flag = False
        while current != None and not flag:
            if current.get_value() == value:
                flag = True
            else:
                current = current.get_next()
        return flag

    def index(self, value):
        """查询节点在链表中的位置"""
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.get_value() == value:
                found = True
            else:
                current = current.get_next()
        if found:
            return count
        else:
            raise ValueError('%s is not in linkedlist' % value)

    def remove(self, value):
        """根据元素值在链表中删除节点"""
        current = self._head
        pre = None
        while current != None:
            if current.get_value() == value:
                if not pre:
                    self._head = current.get_next()
                else:
                    pre.set_next(current.get_next())
                    break
            else:
                pre = current
                current = current.get_next()


if __name__ == "__main__":
    linkedlist = LinkedList()
    print(linkedlist.is_empty())
    print(linkedlist._head.get_value())
    linkedlist.append(1)
    linkedlist.append(2)
    print(linkedlist.search(1))
    print(linkedlist.index(2))
    print(linkedlist.size())