# mkcert使用

## 安装

### windows安装

```shell
choco install mkcert
```

### ubuntu安装

1. 首先安装certutil

```shell
sudo apt install libnss3-tools -y
```

2. 下载二进制安装包

```shell
sudo wget https://github.com/FiloSottile/mkcert/releases/download/v1.4.3/mkcert-v1.4.3-linux-amd64 -O /usr/local/bin/mkcert && \
sudo chmod +x /usr/local/bin/mkcert
```

## 创建证书并安装

```shell
# 创建
mkcert localhost 127.0.0.1 ::1 xinshang
# 安装
mkcert -install
```

> 参考资料
> [本地https快速解决方案——mkcert](https://www.jianshu.com/p/7cb5c2cffaaa)