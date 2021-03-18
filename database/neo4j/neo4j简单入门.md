# 图数据库 `neo4j`

**知识图谱**由于其数据包含实体、属性、关系等，关系型数据库不能很好的体现数据的这些特点，因此知识图谱数据的存储一般是采用图数据库（Graph Databases）。 `neo4j` 是最常见的图数据库。

## 使用

在浏览器中打开以下网址 `http://localhost:7474/browser/` ，记得输入之前设置的账号和密码

在页面的最上方中就可以编写 cypher 语句了

![cypher编辑器](https://i.loli.net/2021/01/21/bN5S7rHTMZLgVsP.png)

`cypher` 语言是 `neo4j` 的声明式图形查询语言，允许用户在不编写图形结构的遍历代码就可以对图形数据进行高效查询。它可以进行创建、更新、删除节点和关系等操作。

## 实战操作

这个案例的节点主要包括人物和城市两类，人物和人物之间有朋友、夫妻等关系，人物和城市之间有出生地的关系。

* 首先删除数据库中的历史数据，确保无干扰数据。

``` cypher
match (n) detach delete n
```

或者

~~这种方法有问题~~

``` cypher
MATCH (n)-[r]-() DELETE n,r
```

这里的 `match` 是匹配操作，小括号代表一个节点， `n` 为标识符

* 接着，创建一个人物节点

``` cypher
create (n:Person {name:'John'}) return n
```

`create` 是创建操作， `Person` 是标签，代表节点的类型。 `{}` 是节点的属性。

创建更多的人物节点

``` cypher
create (n:Person {name:'Sally'}) return n;
create (n:Person {name:'Steve'}) return n;
create (n:Person {name:'Mike'}) return n;
create (n:Person {name:'Liz'}) return n;
create (n:Person {name:'Shawn'}) return n;
```

如图所示，6 个人物节点创建成功

![人物节点](https://i.loli.net/2021/01/21/Gf8nQvUqaTbZse1.png)

* 接下来创建地区节点

``` cypher
create (n:Location {city:'Miami', state:'FL'});
create (n:Location {city:'Boston', state:'MA'});
create (n:Location {city:'Lynn', state:'MA'});
create (n:Location {city:'Portland', state:'ME'});
create (n:Location {city:'San Francisco', state:'CA'});
```

如图所示，5 个地区节点创建成功

![地区节点](https://i.loli.net/2021/01/21/oQ1P9frWMVeOdth.png)

* 接下来创建关系

``` cypher
match (a:Person {name: 'Liz'}), (b:Person {name: 'Mike'}) merge (a)-[:FRIENDS]->(b)
```

这里的方括号 `[]` 表示关系，FRIENDS 是关系的类型。箭头是指关系的方向，这里表示从 a 到 b。

如下图所示

![创建关系](https://i.loli.net/2021/01/21/5SPpAajwbFU1vRz.png)

* 为关系添加属性

``` cypher
match (a:Person {name:'Shawn'}), (b:Person {name:'Sally'}) merge (a)-[:FRIENDS {since:2001}]->(b)
```

跟上面的节点属性一样， `{}` 为关系属性。

![关系的属性](https://i.loli.net/2021/01/21/FsRog6mhU41zB7C.png)

* 添加更多的关系

``` cypher
match (a:Person {name:'Shawn'}), (b:Person {name:'John'}) merge (a)-[:FRIENDS {since:2012}]->(b);
match (a:Person {name:'Mike'}), (b:Person {name:'Shawn'}) merge (a)-[:FRIENDS {since:2006}]->(b);
match (a:Person {name:'Sally'}), (b:Person {name:'Steve'}) merge (a)-[:FRIENDS {since:2006}]->(b);
match (a:Person {name:'Liz'}), (b:Person {name:'John'}) merge (a)-[:FRIENDS {since:1998}]->(b);
```

如图，人物关系图已经建立好

![人物关系图](https://i.loli.net/2021/01/21/gS3bfQieZyaIvWz.png)

* 接下来，我们建立不同类型节点之间的关系，即人物和地点的关系

``` cypher
match (a:Person {name:'John'}), (b:Location {city:'Boston'}) merge (a)-[:BORN_IN {year:1978}]->(b)
```

下图是跟 `John` 节点有关系的节点

![John的关系](https://i.loli.net/2021/01/21/5LmUKry4pkTzl3O.png)

* 同样建立更多人的出生地

``` cypher
match (a:Person {name:'Liz'}), (b:Location {city:'Boston'}) merge (a)-[:BORN_IN {year:1981}]->(b);
match (a:Person {name:'Mike'}), (b:Location {city:'San Francisco'}) merge (a)-[:BORN_IN {year:1960}]->(b);
match (a:Person {name:'Shawn'}), (b:Location {city:'Miami'}) merge (a)-[:BORN_IN {year:1960}]->(b);
match (a:Person {name:'Steve'}), (b:Location {city:'Lynn'}) merge (a)-[:BORN_IN {year:1970}]->(b);
```

至此，所有的关系都已经创建好了

![所有的节点和关系](https://i.loli.net/2021/01/21/GLt2a7zbVXCOqwB.png)

* 接下来我们开始做查询操作，查询所有在 Boston 出生的人

``` cypher
match (a:Person)-[b:BORN_IN]-(c:Location {city:'Boston'}) return a, b, c
```

![在Boston出生的人](https://i.loli.net/2021/01/21/euCpNPIQlzUWrXq.png)

* 查询对外有关系的节点

注意这里是两个短横线

``` cypher
match (a)-->() return a
```

![对外关系图](https://i.loli.net/2021/01/21/LelVqZ7rI9F6waD.png)

* 查询所有有关系的节点

``` cypher
match (a)--() return a
```

![关系节点](https://i.loli.net/2021/01/21/3KrVjCPl1HhAJRX.png)

* 查询所有对外有关系的节点，以及关系类型

``` cypher
match (a)-[r]->(b) return a.name, type(r)
```

![节点名称和关系类型](https://i.loli.net/2021/01/21/NbQcvDOu3hsqHwd.png)

* 查询所有有结婚关系的节点

``` cypher
match (n)-[:MARRIED]-() return n
```

没有查询结果

* 在创建的节点的时候顺便创建好关系

``` cypher
create (a:Person {name: "Todd"})-[:FRIENDS]->(b:Person {name: "Carlos"})
```

![创建节点和关系](https://i.loli.net/2021/01/21/DmzRtJowc8n932r.png)

* 查找某人的朋友的朋友

``` cypher
match (a:Person {name:'Mike'})-[r1:FRIENDS]->(friend)-[r2:FRIENDS]->(friend_of_friend:Person) return a,r1,friend,r2,friend_of_friend
```

![关系的关系的图](https://i.loli.net/2021/01/21/zKYGrbNqQtd6y5f.png)

![关系的关系的表](https://i.loli.net/2021/01/21/TxwJE28KyiLWjdt.png)

* 增加节点的属性

``` cypher
match (a:Person {name:'Liz'}) set a.age=34;
match (a:Person {name:'Shawn'}) set a.age=32;
match (a:Person {name:'John'}) set a.age=44;
match (a:Person {name:'Mike'}) set a.age=25;
```

这里的 set 是设置属性的值

![节点名和属性别名](https://i.loli.net/2021/01/21/CZYa7iQgvMbLDzJ.png)

* 查询具有某属性的节点，并设置别名

``` cypher
match (a:Person) where exists (a.age) return a.name as Name, a.age as Age;
```

这里的 where 是条件，exists 是判断属性是否存在，as 是设置别名

* 删除节点的属性

``` cypher
match (a:Person {name:'Mike'}) set a.test='test';
```

``` cypher
match (a:Person {name:'Mike'}) remove a.test;
```

* 删除节点

``` cypher
match (a:Location {city:'Portland'}) delete a;
```

* 删除有关系的节点

``` cypher
match (a:Person {name:'Todd'})-[rel]-(b:Person) delete a,b,rel;
```
