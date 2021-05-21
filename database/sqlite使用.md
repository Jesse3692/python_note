# sqlite 的使用

## 常用语句

查看所有的表名：`select name from sqlite_master where type='table' order by name;`
查看表的字段：`PRAGMA table_info([tablename]);`
