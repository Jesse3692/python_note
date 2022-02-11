# adb使用

安装： `scoop install adb`

## 准备工作

1. 开发者选项——USB调试

2. 连接夜神模拟器：

端口号可以查看对应安卓系统下的文件：`"D:\Program Files\Nox\bin\BignoxVMS\Nox_3\Nox_3.vbox"`

```shell
adb connect 127.0.0.1:62001 # 或者adb connect 127.0.0.1:52001
```

3. 查看已连接的设备：

```shell
adb devices -l
```

4. 上传数据

```shell
adb push 源文件  目标路径
```

## 安装应用

```shell
 adb install -r .\MT-mytoken-hk-release-3.2.1_mytoken_aligned_signed.apk
```

## 网易mumu

andriod6，个人证书可以解密https信息

## 抓包

使用fiddler classic抓包

手机wlan设置fiddle代理

## 常用命令

```shell
# 查看已安装应用列表 adb shell cmd package list packages
adb shell pm list package # findstr.exe jingdong => package:com.jingdong.app.mall

# 查看当前应用的activity
adb shell "dumpsys window | grep mCurrentFocus"

# 查看安卓系统版本
adb shell getprop ro.build.version.release

# 查看app的版本
adb shell pm dump io.appium.settings | findstr "version"

# 打开app（短信）
com.android.mms/com.android.mms.ui.MmsTabActivity
```