# scoop使用

## 设置代理

```shell
scoop config proxy 127.0.0.1:7890
```

## 常用命令

```shell
# 列出已安装的所有包
scoop list

# 检查问题
scoop checkup

# 安装

scoop install aria2
```

## 常用软件

- make
- gcc
- vim
- gdb
- mysql
- dotnet core
- java
- python
- nodejs
- go
- vscode
- android-sdk

## 添加bucket

在 Scoop 里面，bucket 就是一个软件仓库。

```shell
# 添加
scoop bucket add extras

# scoop直接识别的bucket
scoop bucket known


```

## 常用仓库

- `extras`： Scoop 官方维护的一个仓库，涵盖了大部分因为种种原因不能被收录进主仓库的常用软件
- `nirsoft`：NirSoft 开发的小工具的安装合集
