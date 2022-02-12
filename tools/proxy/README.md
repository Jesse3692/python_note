# 代理使用

## curl下载使用代理

```shell
curl --proxy 192.168.1.25:4780 -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

## git下载仓库使用地址

```shell
git clone -c http.proxy="192.168.1.25:4780" https://github.com/mainflux/ui.git
```