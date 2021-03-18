# -*- encoding: utf-8 -*-
'''
@File    : Stack.py
@Time    : 2020/04/27 13:35:04
@Author  : Jesse Chang
@Contact : jessechang2358@gmail.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : 数据结构-实现一个栈
'''


class Stack:
    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def push(self, element):
        """进栈，向栈压入一个元素"""
        if len(self.stack) >= self.limit:
            raise Exception("Stack Overflow Exception")
        else:
            self.stack.append(element)

    def pop(self):
        """退栈，从栈中弹出一个元素"""
        if self.stack:
            return self.stack.pop()
        else:
            raise Exception("Stack Empty Exception")

    def is_empty(self):
        """判断栈是否为空"""
        return not bool(self.stack)

    def peek(self):
        """查看栈顶元素"""
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError('Stack index out of range')

    def size(self):
        """查看栈的大小"""
        return len(self.stack)

    def clear(self):
        """清空栈中的元素"""
        self.stack = []

    def __str__(self):
        return "<Stack>" + str(self.stack)
