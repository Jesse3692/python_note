# httie使用

发送POST请求：

```shell
http post :5000
```

``` shell

http -f http://localhost:5000 user=admin pwd=123

可以简写网络地址为：localhost:5000或者：5000
```

发送PUT json：

``` shell
http PUT http://localhost:5000 user=admin pwd:=123 a:=true b:='["a","b"]'
```

