# Databases

## `neo4j`

**知识图谱**由于其数据包含实体、属性、关系等，关系型数据库不能很好的体现数据的这些特点，因此知识图谱数据的存储一般是采用图数据库（Graph Databases）。`neo4j`是最常见的图数据库。

neo4j 简单入门


## `mongodb`

> MongoDB shell version v3.4.19
> connecting to: mongodb://127.0.0.1:27017
> MongoDB server version: 3.4.19
> NoSQLBooster: 6.0.4

### 简介

Mongodb 是一款非关系型数据库，非关系型数据库就是把数据直接放进一个大仓库，不标号、不连线、单纯的堆起来。

mongodb 是一个介于关系数据库和非关系数据库之间的产品，是非关系数据库中功能最丰富、最像关系数据库的。

mongodb 支持的数据结构非常松散，是类似 json 的 bson 格式，因此可以存储比较复杂的数据类型。

mongodb 与 mysql 的比较：

| mysql  | mongodb |
| :----: | :-----: |
| 数据库 | 数据库  |
|   表   |  集合   |
|  记录  |  文档   |



### 概念：数据库，文档，集合，元数据

**数据库**：一个 mongodb 可以创建多个数据库，库名规范：不能有空格、点号和$符

**文档**：文档是 mongodb 的核心，类似于关系型数据库的每一行数据。多个键及其关联的值放在一起就是文档。文档之间的逻辑关系：嵌入式关系，比较适合一对一的关系；引用式关系，比较适合一对多或者多对多的情况。

**集合**：集合就是一组文档的组合，就相当于是关系数据库中的表，在 mongodb 中可以存储不同的文档结构的文档。mongodb 在存储信息时，将字段名存储多次，每一条记录都会存储一次字段名，比较好的解决办法就是采用尽可能短的字段名。

**元数据**：数据库的信息存储在集合中，他们统一使用系统的命名空间： `DBNAME.system.*`

DBNAME 可用 db 或数据库名替代：

* DBNAME.system.namespaces 列出所有名字空间
* DBNAME.system.indexs 列出所有索引
* DBNAME.system.profile 列出数据库概要信息
* DBNAME.system.users 列出访问数据库的用户
* DBNAME.system.sources 列出服务器信息



### mongodb使用

[mongodb使用](.\mongodb\README.md)