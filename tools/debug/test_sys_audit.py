"""审计事件"""

import sys


def audit(event, *args):
    """打印事件和参数"""
    print(f'event: {event}; args: {args}')


sys.addaudithook(audit)

with open('test.txt', 'w+', encoding='utf-8') as f:
    f.write('hello')
