# mongodb

使用mongodb shell连接到数据库

```shell
mongosh "mongodb://212.64.7.6:27017/lick-dog?authSource=admin" --username root --authenticationDatabase admin
```

## 基础命令

### 数据库的操作

查询所有数据库

```shell
show dbs;
```

切换/创建数据库

```shell
use yourdb;
```

查看当前连接的数据库

```shell
db
```

删除数据库

```shell
db.dropDatabase();
```

### 集合的操作

查询所有集合

```shell
show collections;
```

创建集合

```shell
db.createCollection("mycollection");
```

删除集合

```shell
db.mycollection.drop();
```

## 数据操作

### 插入数据

使用 `insert` `insertOne`, `insertMany`, `updateOne`, or `updateMany`插入数据，在插入数据的同时创建集合

#### insert

```js
db.users.insertOne({ _id: 2, name: "tom", email: "tom1@qq.com" });
```

```js
db.users.insert([{ _id: 4, name: "jim", email: "jim@qq.com" }, { _id: 3, name: "tom", email: "tom@qq.com" }]);
```

```js
db.users.insertMany([{ _id: 6, name: "jim", email: "jim@qq.com" }, { _id: 7, name: "tom", email: "tom@qq.com" }]);
```

![](https://gitee.com/Jesse3692/vnote_image/raw/master/294611214211359.png)

#### update

```js
db.users.updateOne({ _id: 2}, {$set:{name: "tom1"}});
```

![](https://gitee.com/Jesse3692/vnote_image/raw/master/509601914211498.png)

```js
db.users.updateMany({ name: "jim"}, {$set:{name: "jim1"}});
```

![](https://gitee.com/Jesse3692/vnote_image/raw/master/330342214223588.png)

### 查询数据

#### find

**用法**： `db.COLLECTION_NAME.find()`

``` js
> use post
>
db.post.insert([{
        title: 'MongoDB Overview',
        description: 'MongoDB is no sql database',
        by: 'mongodb',
        url: 'http://www.mongodb.com',
        tags: ['mongodb', 'database', 'NoSQL'],
        likes: 100
    },
    {
        title: 'NoSQL Database',
        description: "NoSQL database doesn't have tables",
        by: 'mongodb',
        url: 'http://www.mongodb.com',
        tags: ['mongodb', 'database', 'NoSQL'],
        likes: 20,
        comments: [{
            user: 'user1',
            message: 'My first comment',
            dateCreated: new Date(2013, 11, 10, 2, 35),
            like: 0
        }]
    }
])
```

查询数据，不加任何参数默认返回所有数据记录：

``` js
> db.post.find()
```

这种写法会导致，大量的数据传输，造成服务器响应迟缓

##### 比较运算符

``` js
> db.post.find({
    "likes": {
        $gt: 10
    },
    $or: [{
            by: "mongodb"
        },
        {
            title: "MongoDB Overview"
        }
    ]
})
```

* `$gt` ：大于 greater than
* `$lt` ：小于 less than
* `$gte` ：大于等于 greater than equal
* `$lte` ： 小于等于 less than equal

##### 模糊查询

mongodb 的模糊查询可以使用正则匹配的方式实现：

``` mongodb

# 以'start'开头的匹配
{"name":/^start/}
# 以'tail'结尾的匹配
{"name":/tail$/}
```

**实践**：

插入以下数据：

``` js
> use student

    >
    db.student.insert([{
            name: "张三",
            age: 18,
            gender: "男"
        },
        {
            name: "李雷",
            age: 25,
            gender: "男"
        },
        {
            name: "韩梅梅",
            age: 23,
            gender: "女"
        } {
            name: "张益达",
            age: 20,
            gender: "男"
        }
    ])
```

查询学生库，学生集合中姓张且年龄不小于 20 岁的男同学

``` js
db.student.find({
    name: /^张/,
    age: {
        $gte: 20
    },
    gender: "男",
});
```

##### 条件操作符 1

mongodb 中的条件操作符有：

* `$gt` ：大于 greater than
* `$lt` ：小于 less than
* `$gte` ：大于等于 greater than equal
* `$lte` ： 小于等于 less than equal

``` js
> db.post.find({
        user_id: {
            $gt: 1
        }
    }) >
    db.post.find({
        user_id: {
            $lte: 2,
            $gt: 1
        }
    })
```

##### 条件操作符 2

语法： `$type:[key]`

key 的值如下：

* 1：双精度型（Double）
* 2：字符串（String）
* 3：对象（Object）
* 4：数组（Array）
* 5：二进制数据（Binary data）
* 7：对象 ID（Object id）
* 8：布尔类型（Boolean）
* 9：日期（Date）
* 10：空（Null）
* 11：正则表达式（Regular Expression）
* 13：JS 代码（JavaScript）
* 14：符号（Symbol）
* 15：有作用域的 JS 代码（JavaScript with scope）
* 16：32 位整型数（32-bit integer）
* 17：时间戳（Timestamp）
* 18：64 位整型数（64-bit integer）
* -1：最小值（Min key）
* 127：最大值（Max key）

``` js
> db.post.find({
    "name": {
        $type: 2
    }
})
等同于
    >
    db.post.find({
        "name": {
            $type: 'string'
        }
    })
```

##### limit()与 skip()

读取指定数量的数据记录 `limit()`

``` js
> db.post.find().limit(1)
```

读取一条记录，默认是排在最前面的那一条数据被读取。

读取数据时跳过指定数量的数据记录 `skip()`

``` js
> db.post.find().limit(1).skip(1)
```

##### 排序 sort()

mongodb 中的排序有升序和降序，其中升序用 1 表示，降序用-1 表示

语法： `db.COLLECTION_NAME.find().sort({KEY:1|-1})`

``` js
> db.post.find().sort({
    "time": 1
})
```

#### 索引 ensureIndex()

索引通常能够极大的提高查询的效率，如果没有索引，mongodb 在读取数据的时候必须扫描集合中的每个文件并选取那些符合查询条件的记录，而这种扫描全集合的查询效率是非常低的，特别是在处理大量的数据时，查询可能要花费几十秒甚至几分钟，这无疑对网站的性能是非常致命的。

索引是特殊的数据结构，索引存储在一个易于遍历读取的数据集合中，索引是对数据库集合中一个文档或者多个文档的值进行排序的一种结构。

语法： `db.COLLECTION_NAME.ensureIndex({KEY:1|-1})`

跟上面排序同样，1 代表升序，-1 代表降序

``` js
> db.post.ensureIndex({
    "name": 1
})
```

`ensureIndex()` 的可选参数：

|        参数        |     类型      |                       描述                       |
| :----------------: | :-----------: | :----------------------------------------------: |
|     background     |    Boolean    | 建立索引时要不要阻塞其他数据库操作，默认为 false |
|       unique       |    Boolean    |          建立的索引是否唯一，默认 false          |
|        name        |    String     |        索引的名称，若未指定，系统自动生成        |
|      dropDups      |    Boolean    |   建立唯一索引时，是否删除重复记录，默认 false   |
|       sparse       |    Boolean    |   对文档不存在的字段数据不启用索引，默认 false   |
| expireAfterSeconds |    Integer    |           设置集合的生存时间，单位为秒           |
|         v          | Index version |                   索引的版本号                   |
|      weights       |   Document    |           索引权重值，范围为 1 到 9999           |
|  default-language  |    String     |                    默认为英语                    |
| language_override  |    String     |                默认值为 language                 |

``` js
> db.post.ensureIndex({
    "user_id": 1,
    "name": 1
}, {
    background: 1
})
```

#### 聚合 aggregate()

语法：

``` js
db.COLLECTION_NAME.aggregate({
    $match: {
        x: 1
    },
    {
        limit: NUM
    },
    $group: {
        _id: $age
    }
})
```

参数：

* `$match`：查询，跟 find 一样
* `$limit`：限制显示结果数量
* `$skip`：忽略结果数量
* `$sort`：排序
* `$group`：按照给定表达式组合结果

``` js
> db.post.aggregate([{
    $group: {
        _id: "$name",
        user: {
            $sum: "$user_id"
        }
    }
}])
```

`$name` 意为取得 name 的值，然后再使用 `$user_id` 取得 user_id 的值并使用 `$sum` 进行求和运算

![image-20200712115751048](https://i.loli.net/2020/07/12/nVFwQEhrg5dsXUa.png)

**聚合表达式**：

|    名称     |                    描述                    |
| :---------: | :----------------------------------------: |
| `$sum` |                  计算总和                  |
| `$avg` |                 计算平均值                 |
| min 和 max  |             计算最小值和最大值             |
| `$push` |        在结果文档中插入值到一个数组        |
| `$addToSet` | 在结果文档中插入值到一个数组，但不创建副本 |
| `$first` |   根据资源文档的排序获取到第一个文档数据   |
| `$last` |  根据资源文档的排序获取到最后一个文档数据  |

**管道**：

mongodb 的聚合管道将 mongodb 文档在一个管道处理完毕后将结果传递给下一个管道处理。管道操作时可以重复的。

表达式：处理输入文档并输出。表达式是无状态的，只能用于计算当前聚合管道的文档，不能处理其它的文档。

聚合框架中常用的几个操作：

* `$project`：修改输入文档的结构。可以用来重命名、增加或删除域，也可以用于创建计算结果以及嵌套文档
* `$match`：用于过滤数据，只输出符合条件的文档。`$match`使用 mongodb 的标准查询操作
* `$limit`：用来限制 mongodb 聚合管道返回的文档数
* `$skip`：在聚合管道中跳过指定数量的文档，并返回余下的文档
* `$unwind`：将文档中的某一个数组类型字段拆分为多条，每条包含数组中的一个值
* `$group`：将集合中的文档分组，可用于统计结果
* `$sort`：将输入文档排序后输出
* `$geoNear`：输出接近某一地理位置的有序文档

``` js
> db.post.aggregate([{
    $match: {
        user_id: {
            $gt: 0,
            $lte: 2
        }
    }
}, {
    $group: {
        _id: "user",
        count: {
            $sum: 1
        }
    }
}])

{
    "_id": "user",
    "count": 2
}
```

![image-20200712142233209](https://i.loli.net/2020/07/12/YbH8iMBuZvp95et.png)