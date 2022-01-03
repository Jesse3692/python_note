# docker的使用

## docker for windows 遇到的问题

docker 每次开机启动不起来也没法关闭
![输入图片说明](https://images.gitee.com/uploads/images/2021/0531/091523_5fe64ef0_1548957.png "屏幕截图.png")
![输入图片说明](https://images.gitee.com/uploads/images/2021/0531/091441_e295326f_1548957.png "屏幕截图.png")

后来经过一系列的操作后也没解决这个问题，后来可以使用以下命令来切换下 Daemon：

```bat
cd "C:\Program Files\Docker\Docker"
DockerCli.exe -SwitchDaemon
@REM 延迟三秒，并且不被键盘输入中断延时
timeout /T 5 /NOBREAK
DockerCli.exe -SwitchDaemon
```

再到后面发现如果不开机启动，等开机完成后再进行启动则不会出现以上的问题。

## 安装docker-compose

```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
