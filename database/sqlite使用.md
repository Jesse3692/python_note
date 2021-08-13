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
