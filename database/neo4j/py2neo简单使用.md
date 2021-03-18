# py2neo使用

- [创建节点和关系](#创建节点和关系)
- [添加属性](#添加属性)
- [添加默认属性](#添加默认属性)
- [批量更新属性](#批量更新属性)
- [子图Subgraph的使用](#添加数据)

## 创建节点和关系

``` python
from py2neo import Node, Relationship,Graph
```

``` python
graph = Graph('bolt://localhost:7687',username='neo4j', password='123456')
```

``` python
alice = Node('Person', name='Alice')
bob = Node('Person', name='Bob')
relationship = Relationship(alice, 'KNOWS', bob)
print(alice, bob, relationship)
```

``` text
    (:Person {name: 'Alice'}) (:Person {name: 'Bob'}) (Alice)-[:KNOWS {}]->(Bob)
```

### 添加属性

Node和Relationship都继承了PropertyDict类，它可以赋值很多属性，类似于字典的形式。

``` python
alice['age'] = 20
bob['age'] = 21
relationship['time'] = '2020/02/02'
print(alice, bob, relationship)
```

``` text
(:Person {age: 20, name: 'Alice'}) (:Person {age: 21, name: 'Bob'}) (Alice)-[:KNOWS {time: '2020/02/02'}]->(Bob)
```

### 添加默认属性

也可以通过类似字典的方式，使用setdefault添加默认属性

``` python
alice.setdefault('location', '北京')
print(alice)
```

``` text
    (:Person {age: 20, location: '\u5317\u4eac', name: 'Alice'})
```

可见没有给alice对象赋值location属性，它就会使用默认属性。

``` python
alice['location'] = '上海'
alice.setdefault('location', '北京')
print(alice)
```

``` text
    (:Person {age: 20, location: '\u4e0a\u6d77', name: 'Alice'})
```

但是如果赋值了location属性，那么它就会覆盖默认属性

### 批量更新属性

``` python
data = {
    'name':'Amy',
    'age':21
}

alice.update(data)
print(alice)
```

``` text
   (:Person {age: 21, location: '\u4e0a\u6d77', name: 'Amy'})
```

旧有的属性会被保留，新旧都有的会被更新

## Subgraph 子图

子图是Node和Relationship的集合，最简单的构造子图的方式是通过关系运算符

``` python
from py2neo import Node, Relationship
```

``` python
alice = Node('Person', name='Alice')
bob = Node('Person', name='Bob')
relationship = Relationship(alice, 'KNOWS', bob)
sub_graph = alice | bob | relationship
print(sub_graph)
```

``` text
    Subgraph({Node('Person', name='Alice'), Node('Person', name='Bob')}, {KNOWS(Node('Person', name='Alice'), Node('Person', name='Bob'))})
```

### 添加数据

其实上面的一系列操作，都没有实际保存到neo4j数据库中

``` python
from py2neo import Node,Graph
```

``` python
graph = Graph('bolt://localhost:7687', username='neo4j', password='123456')
transaction = graph.begin()
```

``` python
alice = Node('Person', name='Alice', location='北京', age=21)
bob = Node('Person', name='Bob', location='上海', age=22)
mike = Node('Person', name='Mike', location='重庆', age=21 )
```

``` python
transaction.create(alice | bob | mike)
transaction.commit()
```

 `<Bookmark 'FB:kcwQpR792zMVRG6xUlW8tVwKOWiQ'>`

![created nodes](https://i.loli.net/2021/01/23/z8O7h1xk3KZ9VIJ.png)

### 查询数据

使用node和relationship数据类型自带的匹配属性

``` python
from py2neo import Graph
```

``` python
graph = Graph('bolt://localhost:7687', username='neo4j', password='123456')
```

``` python
# TODO 据说是效率较慢，没测试过
result = graph.nodes.match('Person', age=21)
print(list(result))
```

``` Python
# Python
    [Node('Person', age=21, location='北京', name='Alice'), Node('Person', age=21, location='重庆', name='Mike')]
```

使用查询模块

``` python
from py2neo import Graph
from py2neo.matching import NodeMatcher
```

``` python
graph = Graph('bolt://localhost:7687', username='neo4j', password='123456')
node_matcher = NodeMatcher(graph=graph)
```

``` python
# 写法一
result = node_matcher.match('Person', age=21)
print(list(result))
```

``` text
    [Node('Person', age=21, location='北京', name='Alice'), Node('Person', age=21, location='重庆', name='Mike')]
```

``` python
# 写法二
result = node_matcher.match('Person').where(age=21)
print(list(result))
```

``` text
    [Node('Person', age=21, location='北京', name='Alice'), Node('Person', age=21, location='重庆', name='Mike')]
```

上面的几个操作就相当于：

``` cypher
match (p:Person) where p.age=21 return p
```

``` python
# 取第一个
result = node_matcher.match('Person', age=21).first()
print(result)
```

``` text
    (_10:Person {age: 21, location: '\u5317\u4eac', name: 'Alice'})
```

``` cypher
match (p:Person) where p.age=21 return p limit 1
```

以上的py2neo匹配，其缺点在于匹配被人为的分割成了节点和关系的匹配，使用起来不够灵活，因为节点和关系的匹配常常是紧密关联的。不如原生的cypher灵活，它没有限定类型
