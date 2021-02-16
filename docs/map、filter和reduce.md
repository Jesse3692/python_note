# map、filter和reduce

## map

map会将一个函数映射到一个输入列表的所有元素上。

 `map(function_to_apply, list_of_inputs)`

特殊用法（同时执行多个函数）：

``` Python
def multiply(x):
    return (x*x)
def add(x):
    return (x+x)
funcs = [multiply, add]

for i in range(5):
    value = map(lambda x: x(i), funcs)
    print(list(value))
```

## filter

filter过滤列表中的元素，并且返回一个由所有符合要求的元素所组成的列表。

``` Python
number_list = range(-5, 5)
less_than_zero = filter(lambda x:x<0, number_list)
print(list(less_than_zero))
```

## reduce

reduce()函数会对参数序列中的元素进行累积

函数将一个数据集合（列表，元组等）中的所有数据进行下列操作：用传给reduce中的函数function先对集合中的第1、2个元素进行操作，得到的结果再与第三个数据用function函数运算，最后得到一个结果。

当需要对一个列表进行一些计算并返回结果时，reduce是一个非常有用的函数。

``` Python
from functools import reduce
product = reduce((lambda x,y: x*y), [1,2,3,4])
print(product)  # >> 24 1*2>>2*3>>6*4
```
