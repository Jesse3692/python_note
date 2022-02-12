# nodejs 使用

## 全局变量 process

- process.argv 是命令行参数数组，第一个元素是 node，第二个元素是脚本文件名，从第三个元素开始每个元素是一个运行参数。

- process.stdout 是标准输出流

- process.stdin 是标准输入流

- process.nextTick(callback)的功能是为事件循环设置一项任务

- process.platform

- process.pid

- process.execPath

- process.memoryUsage()

## 控制台标准输出 console

- console.log

- console.error

- console.trace

## 常用工具 util

- util.inherits（已弃用）

- util.inspect(object,[showHidden],[depth], [colors])将一个任意对象转换为字符串

- util.isArray()

- util.isRegExp()

- util.isDate()

- util.isError()

- util.format()

- util.debug()

## 事件发射器 EventEmitter

events.EventEmitter 事件发射与事件监听器功能的封装

- EventEmitter.on(event, listener)为指定事件注册一个监听器
- EventEmitter.emit(event, [arg1], [arg2],[...])发射 event 事件
- EventEmitter.once(event, listener)为指定事件注册一个单次监听器
- EventEmitter.removeListener(event, listener)移除指定事件的某个监听器
- EventEmitter.removeAllListeners([event])移除所有事件的所有监听器

## 文件系统 fs

- fs.readFile(filename, [encoding], [callback(err, data)])是最简单的读取文件的函数。

- fs.readFileSync(filename, [encoding])是 fs.readFile 同步的版本。

- fs.open(path, flags, [mode], [callback(err, fd)])是 POSIX open 函数的封装

- fs.read(fd, buffer, offset, length, position, [callback(err, bytesRead, buffer)])是 POSIX read 函数的封装

- fs.write(fd, buffer, offset, length, position, [callback(err, bytesWritten, buffer)])写入文件（文件描述符）

- fs.writeFile(filename, data, [encoding], [callback(err)])写入文件内容

- fs.unlink(path, [callback(err)]) 删除文件

- fs.mkdir(path, [mode], [callback(err)]) 创建目录

- fs.rmdir(path, [callback(err)]) 删除目录

- fs.readdir(path, [callback(err, files)]) 读取目录

- fs.realpath(path, [callback(err, resolvePath)]) 获取真实路径

- fs.rename(path1, path2, [callback(err)]) 更名

- fs.truncate(fd, len, [callback(err)]) 截断

- fs.chown(path, uid, gid, [callback(err)]) 更改所有权

- fs.fchown(fd, uid, gid, [callback(err)]) 更改所有权（文件描述符）

- fs.lchown(path, uid, gid, [callback(err)]) 更改所有权（不解析符号链接）

- fs.chmod(path, mode, [callback(err)]) 更改权限

- fs.fchmod(fd, mode, [callback(err)]) 更改权限（文件描述符）

- fs.lchmod(path, mode, [callback(err)]) 更改权限（不解析符号链接）

- fs.stat(path, [callback(err, stats)]) 获取文件信息

- fs.fstat(fd, [callback(err, stats)]) 获取文件信息（文件描述符）

- fs.lstat(path, [callback(err, stats)]) 获取文件信息（不解析符号链接）

- fs.link(srcpath, dstpath, [callback(err)]) 创建硬链接

- fs.symlink(linkdata, path, [type], [callback(err)]) 创建符号链接

- fs.readlink(path, [callback(err, linkString)]) 读取链接

- fs.utimes(path, atime, mtime, [callback(err)]) 修改文件时间戳

- fs.futimes(fd, atime, mtime, [callback(err)]) 修改文件时间戳（文件描述符）

- fs.fsync(fd, [callback(err)]) 同步磁盘缓存
