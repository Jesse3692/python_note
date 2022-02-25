# pip使用

## 查看配置列表

```shell
pip config list
```

## 设置pip镜像（清华）

```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# pip config set global.index-url https://pypi.python.org/simple
```

这样就会自动添加pip配置`C:\Users\Administrator\AppData\Roaming\pip\pip.ini`

## 设置pip代理

```shell
pip config set global.proxy 'http://127.0.0.1:7890'
```

设置pip代理之后，安装包可能还会报错，还需要添加系统环境变量

```powershell
[Environment]::SetEnvironmentVariable("HTTP_PROXY", "http://127.0.0.1:7890", 'User')
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://127.0.0.1:7890", 'User')
```

## 离线下载包及其依赖

```shell
pip download -d save_path packages
```


