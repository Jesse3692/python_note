# dict字典

## 字典的常用操作

访问字典的值：dict.get(key, None),这样不会报错

返回删除的key所对应的value值：value = dict.pop(key)

删除单个元素：del dict[key]

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