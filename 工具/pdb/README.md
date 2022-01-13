# pdb使用

```shell
sudo apt install python3.8-dbg
```

常用命令

```shell

############################################## 内存相关 ##############################################
info proc

i proc mappings # 进程的内存映射信息
# 更详细地输出进程的内存信息，包括引用的动态链接库
i files # 等价 i target
info proc files -- List files opened by the specified process.
info proc mappings -- List memory regions mapped by the specified process.
info proc stat -- List process info from /proc/PID/stat.
info proc status -- List process info from /proc/PID/status.
############################################## 内存相关 ##############################################

# 查看当前的线程
info threads

bt

py-bt

# 链接到目标进程
gdb python 314474 # 等价(gdb) attach 314474


generate-core-file
gdb python core.<pid>

# n、f、u 都是可选的参数，其中，n 是一个正整数，表示显示内存的长度，也就是说从当前地址向后显示几个地址的内容；f 表示显示的格式；u 表示将多少个字节作为一个值取出来，如果不指定的话，GDB默认是4个bytes，如果不指定的话，默认是4个bytes。当我们指定了字节长度后，GDB会从指内存定的内存地址开始，读写指定字节，并把其当作一个值取出来。<addr>表示一个内存地址。
x  /<n/f/u> <addr> 

# 显示代码内容
(gdb) l

############################################## python gdb相关 ##############################################
py-list                 # 查看当前python应用程序上下文
py-bt                   # 查看当前python应用程序调用堆栈
py-bt-full              # 查看当前python应用程序调用堆栈，并且显示每个frame的详细情况
py-print <variable>     # 查看python变量
py-locals               # 查看当前的scope的变量
py-up                   # 查看上一个frame
py-down                 # 查看下一个frame
############################################## python gdb相关 ##############################################

# 设置打印格式
(gdb) set p pretty on

# 打印对象内存分布
(gdb) p d

# 打印对象大小
(gdb) p sizeof(d)
```