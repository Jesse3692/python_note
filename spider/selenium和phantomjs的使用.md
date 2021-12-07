# selenium和phantomjs的使用

## phantomjs使用

下载 [Download PhantomJS](https://phantomjs.org/download.html)

添加环境变量

## Selenium使用

```shell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install selenium==2.48.0
```

**注意：最新版的selenium不再支持PhantomJS驱动**

### 初始化

```python
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# Create a new instance of the PhantomJS driver
driver = webdriver.PhantomJS()

driver.get("http://www.baidu.com")
```

### 简单操作

```python

# Get the snapshot of the current page
# driver.save_screenshot("baidu.png")

# get the text content of the id tag of the current page named "wrapper"
data = driver.find_element_by_id("wrapper").text

# type the text "phantomjs" in the search box
driver.find_element_by_id("kw").send_keys("phantomjs")

# click the search button
driver.find_element_by_id("su").click()

# wait for the page to load
time.sleep(3)
# get the snapshot of the current page
driver.save_screenshot("phantomjs.png")
```

### 按键操作

```python

# ctrl + a to select all the text in the search box
driver.find_element_by_id("kw").send_keys(Keys.CONTROL + "a")

# delete the text in the search box
driver.find_element_by_id("kw").send_keys(Keys.DELETE)

# backspace to delete the text in the search box
driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)

# ctrl + x to cut the text in the search box
driver.find_element_by_id("kw").send_keys(Keys.CONTROL + "x")

# ctrl + v to paste the text in the search box
driver.find_element_by_id("kw").send_keys(Keys.CONTROL + "v")

# enter to submit the search
driver.find_element_by_id("su").send_keys(Keys.ENTER)

# clear the text in the search box
driver.find_element_by_id("kw").clear()
```

### 页面信息

```python
# get the url of the current page
driver.current_url

# get the title of the current page
title = driver.title

# get the source code after the web page rendered
page_source = driver.page_source

# get the cookies of the current page
cookies = driver.get_cookies()
```

### 关闭或退出

```python
# close the current page, if the current page is the last page, the browser will quit automatically
driver.close()

# quit the browser
driver.quit()
```

> 参考资料
> [Python之Selenium+PhantomJS使用详解](https://www.jianshu.com/p/33e295e86319)

