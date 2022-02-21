# npm 使用

## 使用镜像加速

```shell
# 添加taobao npm镜像
npm config set registry https://registry.npm.taobao.org
# 添加taobao electron镜像
npm config set ELECTRON_MIRROR https://npm.taobao.org/mirrors/electron/
```

## 设置 npm 代理

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

## 常用命令

```shell
# 查看本机已安装的全局包
npm list -g --depth 0

# 全局安装
npm install -g appium

# 项目安装-prod
npm install -save appium

# 项目安装-dev
npm install –save-dev appium
```
