# appium 使用

## appium desired capabilities

```json
{
  "deviceName": "2dd34597",
  "platformName": "Android",
  "platformVersion": "11"
}
```

## 获取 app 的控件信息

通过截屏并分析 `XML` 布局文件的方式，为用户提供控件信息查看服务。

### appium desktop

这里使用的版本为`1.15.1`，自带 `appium` 和 `inspector`

需要注意的是，使用自带的 `inspector` 可能会无法连接 session（刚开始可以，后来连接失败），但是使用`Appium Inspector 2021.12.2`和`Appium-Python-Client==0.50`是可以连接的。

### Appium Inspector

这里使用的版本为`2021.12.2`，是独立的软件并不提供 `appium` 服务

### uiautomatorviewer

uiautomatorviewer 是 android SDK 自带的工具，缺点是没法点击操作和刷新

## 控件定位

appium 的控件定位方式是完全遵守 webdriver 的 mobile 扩展协议的。

### 通过 resource id 定位

- 使用`findElement(By.ID,"resourceId")`的方式。这也是原生的 `webdriver` 定义的方法，不过竟然在 appium 的官方文档里没有提及，属于隐藏技；

- 使用`find_elements_by_android_uiautomator('new UiSelector().resourceId("the_id")')`的方式
