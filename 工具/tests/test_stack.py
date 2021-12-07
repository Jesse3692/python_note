# -*- encoding: utf-8 -*-
'''
@File    : test_stack.py
@Time    : 2020/04/23 09:43:06
@Author  : Jesse Chang
@Contact : jessechang2358@gmail.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : 对栈进行测试
'''


import os
import sys

work_dir = os.getcwd()
sys.path.append(work_dir)
print(work_dir)
# print(os.path.abspath(os.path.dirname(__file__)))

import pytest
from Stack import Stack


class TestClass(object):
    """测试抛出的是否为指定异常"""
    def raise_stackoverflow(self):
        stack = Stack(limit=1)
        stack.push('1')
        stack.push('2')
        
    def test_raise_stackoverflow(self):
        with pytest.raises(Exception) as e:
            self.raise_stackoverflow()
        assert 'Stack Overflow Exception' == str(e.value)
    
    def raise_stackempty(self):
        stack = Stack(limit=1)
        stack.pop()
        
    def test_raise_stackempty(self):
        with pytest.raises(Exception) as e:
            self.raise_stackempty()
        assert 'Stack Empty Exception' == str(e.value)
        
    def raise_stackemptypeek(self):
        stack = Stack()
        stack.peek()
        
    def test_raise_stackemptypeek(self):
        with pytest.raises(IndexError) as e:
            self.raise_stackemptypeek()
        assert 'Stack index out of range' == str(e.value)


