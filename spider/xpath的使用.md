# xpath的使用

简单使用

```python
from lxml import etree

selector=etree.HTML(源码) #将源码转化为能被XPath匹配的格式

selector.xpath(表达式) #返回为一列表
```

![](https://gitee.com/Jesse3692/vnote_image/raw/master/428632814228627.png)