# xpath的使用

简单使用

```python
from lxml import etree

selector=etree.HTML(源码) #将源码转化为能被XPath匹配的格式

selector.xpath(表达式) #返回为一列表
```

![](https://i.loli.net/2021/07/24/sLzO6hQr3JcF7eZ.png)