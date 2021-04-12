# python中的编码

## 编码类型

1. ascii. 有: 数字, 字母, 特殊字符. 8bit  1byte 128  最前面是0
2. gbk. 包含: ascii, 中文(主要), 日文, 韩文, 繁体文字. 16bit, 2byte.
3. unicode. 包含gbk,ascii,big5... 32bit, 4byte
4. utf-8. 可变长度的unicode.
    1. 英文: 8bit,1byte
    2. 欧洲文字: 16bit 2byte
    3. 中文: 24bit 3byte

## 编码转换

不同的编码之间不能随意转换. 中国人gbk和德国人utf-8骂 想要沟通必须通过英文(unicode)(媒介)

在python3中. 默认的编码是unicode, 我们的字符串就是unicode
在python2中. 默认的编码是ASCII.  Cpython.c语言的默认编码是ASCII

unicode弊端: 在存储和传输的时候. 是很浪费的
在存储和传输的时候不能直接使用unicode. 必须要对字符串进行编码. 编码成bytes类型
bytes: 字节形式的字符串

    1. encode(编码格式) 编码
    2. decode(编码格式) 解码

bytes是一种另类的字符串表示形式
"哈哈哈" => \xee\xab\x13\xee\xab\x13\xee\xab\x13
