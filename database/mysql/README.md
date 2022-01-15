# MySQL 数据库


使用mysql命令行连接到数据库

```shell
.\mysql.exe -h 212.64.7.6 -P 3306 -u root -p
```

避免sql注入的问题，使用`cursor.execute(sql, (user, pwd))`

## pymysql使用

安装 `pip install pymysql`


