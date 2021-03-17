# -*- encoding: utf-8 -*-
'''
@File    : balanced_parentheses.py
@Time    : 2020/04/23 16:13:59
@Author  : Jesse Chang
@Contact : jessechang2358@gmail.com
@Version : 0.1
@License : Apache License Version 2.0, January 2004
@Desc    : None
'''

import os
import sys
sys.path.append(os.getcwd())

from Stack import Stack

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
            
        
    
if __name__ == "__main__":
    examples = ['(((()))))', '((()))))', '((()))']
    for example in examples:
        print(example + 'is ' + str(balanced_parentheses(example)))