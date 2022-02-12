# nvm使用

## 安装

```shell
scoop install nvm
```

## 配置淘宝镜像源

在配置文件中添加以下内容：

```ini
; "E:\scoop\apps\nvm\1.1.9\settings.txt"
node_mirror: https://npm.taobao.org/mirrors/node/
npm_mirror: https://npm.taobao.org/mirrors/npm/
```

## 常用命令

```shell
# 安装nodejs
nvm install 14.17.3

# 使用nodejs
nvm use 14.17.3
```
