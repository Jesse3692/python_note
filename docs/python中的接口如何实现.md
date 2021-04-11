# python中的接口如何实现

## 使用NotImplementedError

``` Python
# 项目经理
class Base:
    # 对子类进行了约束. 必须重写该方法
    # 以后上班了. 拿到公司代码之后. 发现了notImplementedError 继承他 直接重写他
    def login(self):
        #     没有被实现错误
        raise NotImplementedError("你要重写一下login这个方法. 否则报错!") # 抛异常  .

class Member(Base):
    def login(self):
        print("我是普通人登录")

class BaWu(Base):
    def login(self):
        print("吧务登录")

class Houtai(Base):
    def login(self): # 报错, 上层程序员写代码没有按照规范来
        print("后台登录")

# # 整合这些个功能
def deng(obj):
    obj.login()

m = Member()
bw = BaWu()
ht = Houtai()

deng(m)
deng(bw)
deng(ht)
```

## 使用抽象类

``` Python
# 抽象类和抽象方法 -> java c#
# 抽象方法不需要给出具体的方法体. 抽象方法内只写一个pass就可以了
# 在一个类中如果有一个方法是抽象方法. 那么这个类一定是一个抽象类
# 抽象类中. 如果有抽象方法. 此时这个类不能创建对象
# 如果一个类中所有的方法都是抽象方法. 这个类可以被称为接口类

# 写一个抽象方法:导入一个模块
from abc import ABCMeta, abstractmethod

# 此时抽象类不能创建对象
class Animal(metaclass=ABCMeta): # 写完这东西. 就是个抽象类
    @abstractmethod # 抽象方法
    def chi(self): pass # 吃应该只是一个抽象概念. 没办法完美的描述出来吃什么东西

    # 抽象类中可以有正常的方法
    def dong(self):
        print("动物会动")

# class Cat(Animal): # 此时猫里面也有一个抽象方法, 此时的猫是创建不了对象的
#     pass

class Cat(Animal):
    def chi(self): # 重写父类中的抽象方法
        print("猫喜欢吃鱼")

a = Cat()
a.chi()
a.dong()
```
