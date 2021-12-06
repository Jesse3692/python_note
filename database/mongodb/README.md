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

销毁数据库

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
