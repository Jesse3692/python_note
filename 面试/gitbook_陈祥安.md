# gitbook

## 语言特性

01. 谈谈对 Python 和其他语言的区别

python是一种面向对象的、解释型、强类型、动态的脚本语言。

[强类型与弱类型区别](https://gitee.com/vnote/vnote_python/blob/c645baab09418741e932333c910ce7e49223413f/%E5%BE%85%E6%95%B4%E7%90%86/%E5%BC%BA%E7%B1%BB%E5%9E%8B%E8%AF%AD%E8%A8%80%E4%B8%8E%E5%BC%B1%E7%B1%BB%E5%9E%8B%E8%AF%AD%E8%A8%80.md)

04. Python3 和 Python2 的区别？

## 编程规范

07. 什么是PEP8？

[pep8规范（通俗版）](https://gitee.com/Jesse3692/python_note/blob/1a857c2936f3fe6b5c0db848718466ff4d38aa7f/docs/pep8%E8%A7%84%E8%8C%83.md)

10. 了解类型注解么？

首先python中并没有实现真正的类型注解，这只是辅助IDE以及后期维护的，常见的有形参位置，变量以及返回值。

[静觅-类型注解](https://cuiqingcai.com/7071.html)

18. 例举几个规范 Python 代码风格的工具

pylint 和 flake8 以及 SonarQube工具

[pylint信息](https://gitee.com/vnote/vnote_python/blob/68778103cfb801d7cac4a5a2c157f9b418c22aab/%E5%B8%B8%E7%94%A8%E5%B7%A5%E5%85%B7%E5%92%8C%E6%A8%A1%E5%9D%97/pylint%20messages.md)

## 数据类型-字符串

20. 如何区别可变数据类型和不可变数据类型?

可变和不可变是根据内存地址来说的。

22. 如何检测字符串中只含有数字?

``` Python
>>> a = '123一'
>>> a.isdigit()
False
>>> a.isnumeric()
True
```

24. Python 中的字符串格式化方式你知道哪些？

* %
* format（危险）
* f-string
* 模板字符串

[](https://gitee.com/vnote/vnote_python/blob/4c091f5a5d01af27549ad9107a1e07a5d8945cfa/Document/%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B/%E6%95%B0%E6%8D%AE%E7%B1%BB%E5%9E%8B.md#字符串的格式化操作)
