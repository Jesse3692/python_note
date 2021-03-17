# -*- encoding: utf-8 -*-
'''
@File    : linked_list.py
@Time    : 2020/04/24 09:41:38
@Author  : Jesse Chang
@Contact : jessechang2358@gmail.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : 单链表
'''


class Node:
    def __init__(self, data):
        self.data = data  # 表示对应的元素值
        self.next = None  # 表示下一个链接的链点


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
        # 创建Node数据结构
        node = Node(new_element)
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
            self.head = node

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


if __name__ == "__main__":
    linked_list = Linked_List()
    # a = [1,2,3,4,5,6]
    # linked_list.initlist(a)
    # print(linked_list.print_list())
    linked_list.append(1)
    linked_list.append(2)
    linked_list.print_list()
    # TODO 合并这三个单链表数据结构
