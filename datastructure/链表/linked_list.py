class Node:
    """定义一个node类
    """

    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_value(self, new_value):
        self._value = new_value

    def set_next(self, new_next):
        self._next = new_next


class LinkedList:
    def __init__(self):
        self._head = Node()
        self._tail = None
        self._length = 0

    def is_empty(self):
        """是否为空
        """
        return self._head == None

    def add_first(self, value):
        """在链表前端添加元素 O(1)
        """
        new_node = Node(value, None)

    def append(self, value):
        """在链表的尾部添加元素 O(n)
        """
        new_node = Node(value)
        if self.is_empty():
            self._head = new_node
        else:
            current = self._head  # current 当前元素
            while current.get_next() != None:  # 遍历链表
                current = current.get_next()
            current.set_next(new_node)  # 此时current为链表的最后元素

    def search(self, value):
        """检查元素是否在链表中
        """
        current = self._head
        found_value = False
        while current != None and not found_value:
            if current.get_value() == value:
                found_value = True
            else:
                current = current.get_next()
        return found_value

    # @property
    # def length(self):
    # HACK    """获取链表的长度
    #     """
    #     print('length')
    #     if self._head == None:
    #         print('1')
    #         return 0
    #     current = self._head

    #     count = 1
    #     while current != None:
    #         count += 1
    #         current = current.get_next()
    #     return count

    def index(self, value):
        """元素在链表中的索引
        """
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
            raise ValueError('%s if not in LinkedList' % value)

    def remove(self, value):
        """删除链表中的元素
        """
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

    def insert(self, pos, value):
        """插入元素

        :param pos: 索引
        :param value: 值
        """
        if pos <= 1:
            self.add_first(value)
        elif pos > self._length():
            self.append(value)
        else:
            temp = Node(value)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.get_next()
                pre.set_next(temp)
                temp.set_next(current)


if __name__ == "__main__":
    linked_list = Node()
    print(linked_list.length)
    print(linked_list.is_empty())
