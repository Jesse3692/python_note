# set集合

## 交集（intersection）

``` Python
valid = ['yellow', 'red', 'blue','green', 'black' ]
input_set = set(['red', 'brown'])
print('交集：', input_set.intersection(valid))
```

## 差集（difference）

``` Python
valid = ['yellow', 'red', 'blue','green', 'black' ]
input_set = set(['red', 'brown'])
print(input_set.difference(valid)) # >> {'brown'}
```

``` Python
valid = ['yellow', 'red', 'blue','green', 'black' ]
input_set = set(['red', 'brown'])
print(set(valid).difference(input_set)) # >> {'green', 'yellow', 'black', 'blue'}
```
