# dict字典

## 特殊用法

### 比较两个字典中的内容

```python
a = {'a':1, 'b':2}
b = {'b':2}

# 查看两个字典共有的key或键值对
a.keys() & b.keys()
Out[14]: {'b'}
a.items() & b.items()
Out[15]: {('b', 2)}

# 查看两个字典不共有的key或键值对
a.keys() ^ b.keys()
Out[16]: {'a'}
a.items() ^ b.items()
Out[17]: {('a', 1)}

# 查看在字典a而不在字典b中的key或键值对
a.keys() - b.keys()
Out[18]: {'a'}
a.items() - b.items()
Out[19]: {('a', 1)}
```