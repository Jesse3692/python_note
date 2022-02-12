# uml 的使用

## python 代码生成 UML

### linux

pyreverse -o png -p Pyreverse 文件夹/文件

### windows

将`pyreverse`和`Graphviz`添加到环境变量

[windows 下载地址](https://gitlab.com/graphviz/graphviz/-/package_files/9574245/download)

绘制简单的图（当前文件的）：
pyreverse -o png -p Pyreverse 文件夹/文件

绘制复杂的图（相关联的）：
pyreverse -ASmy -o png .\vnpy\gateway\huobi\huobi_gateway.py

绘制复杂的图（只显示当前项目类的继承关系）：

pyreverse -ASmy -s0 -o png .\vnpy\gateway\huobi\huobi_gateway.py

### 相关参数

- -ASmy 相关联的都显示出来，较为全面，包括第三方的库，比如 tensorflow 等，可能会冗余，较乱。
- -c 选项只追踪一个特定的类，默认会带-ASmy 选项，如果不想让联系显示进来，只显示类的继承关系时，可以另外使用-s0 选项指定（但有时候不会起作用），注意这里的类名要给相对路径下的全名。
- -o 输出的格式，最好选用 pdf 格式，图片格式默认不是矢量图，会看不清。
  只寻求此工程目录下的类关系结构的话，可以只使用-my 参数
- --ignore google 是为了避免生成 google 这个第三方包里面的类
- -a N, -A depth of research for ancestors
- -s N, -S depth of research for associated classes
- -A, -S all ancestors, resp. all associated
- -m[yn] add or remove the module name
- -f MOD filter the attributes : PUB_ONLY/SPECIAL/OTHER/ALL
- -k show only the classes (no attributes and methods)
- -b show 'builtin' objects

example：
pyreverse -my -o pdf <project dir name>
生成结果会保存在当前命令执行的路径下。
