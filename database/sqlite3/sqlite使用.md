# sqlite 的使用

## 安装

```shell
sudo apt install sqlite3
```

## 常用语句

连接数据库：`sqlite3 数据库文件`
查看所有的表：`.tables`
查看表结构：`.schema 数据表`
查看所有的表名：`select name from sqlite_master where type='table' order by name;`
查看表的字段：`PRAGMA table_info([tablename]);`

查看表的结构：
select * from sqlite_master where type="table" and name="coin_record";

结构化的查询结果：

```sql
.header on
.mode column
.timer on

select * from coin_record where coin_parent = 'e145c41b0ee64af18f094664c36345c5d60017a60a2a6104af65e687b1ba9c35';
```
