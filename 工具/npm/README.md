# npm使用

## 使用镜像加速

```shell
# 添加taobao npm镜像
npm config set registry https://registry.npm.taobao.org
# 添加taobao electron镜像
npm config set ELECTRON_MIRROR https://npm.taobao.org/mirrors/electron/
```

## 设置npm代理

```shell
npm config set http-proxy http://127.0.0.1:7890
npm config set https-proxy http://127.0.0.1:7890

# 删除代理
npm config set proxy null
npm config set https-proxy null
```

## 添加环境变量

```powershell
setx /m ELECTRON_MIRROR "https://npm.taobao.org/mirrors/electron/"
```