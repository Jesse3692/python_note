# makefile使用

```makefile
CLANG = clang

EXECABLE = monitor-exec

BPFCODE = bpf_program

BPFTOOLS = /kernel-src/samples/bpf

BPFLOADER = $(BPFTOOLS)/bpf_load.c

CCINCLUDE += -I/kernel-src/tools/testing/selftests/bpf

LOADINCLUDE += -I/kernel-src/samples/bpf
LOADINCLUDE += -I/kernel-src/tools/lib
LOADINCLUDE += -I/kernel-src/tools/perf
LOADINCLUDE += -I/kernel-src/tools/include

LIBRARY_PATH = -L/usr/local/lib64

BPFSO = -lbpf

CFLAGS += $(shell grep -q "define HAVE_ATTR_TEST 1" /kernel-src/tools/perf/perf-sys.h \
                  && echo "-DHAVE_ATTR_TEST=0")

.PHONY: clean $(CLANG) bpfload build

clean:
	rm -f *.o *.so $(EXECABLE)

# clang -O2 -target bpf -c bpf_program.c -I/kernel-src/tools/testing/selftests/bpf -o bpf_program.o
build: $(BPFCODE.c) ${BPFLOADER}
	$(CLANG) -O2 -target bpf -c $(BPFCODE:=.c) $(CCINCLUDE) -o ${BPFCODE:=.o}

# clang -O2 -target bpf -c bpf_program.c -I/kernel-src/tools/testing/selftests/bpf -o bpf_program.o
# clang -DHAVE_ATTR_TEST=0 -o monitor-exec -lelf -I/kernel-src/samples/bpf -I/kernel-src/tools/lib -I/kernel-src/tools/perf -I/kernel-src/tools/include -L/usr/local/lib64 -lbpf \
#         /kernel-src/samples/bpf/bpf_load.c loader.c
bpfload: build
	clang $(CFLAGS) -o $(EXECABLE) -lelf $(LOADINCLUDE) $(LIBRARY_PATH) $(BPFSO) \
	$(BPFLOADER) loader.c

$(EXECABLE): bpfload

.DEFAULT_GOAL := $(EXECABLE)
```

- .DEFAULT_GOAL：GNU Make版本3.81引入了一个名为.DEFAULT_GOAL的特殊变量，可用于告知如果在命令行中未指定目标，应该构建哪个目标（或目标）。否则，Make会简单地使它遇到的第一个目标。

- .PHONY：这样 clean 就被声明成一个伪目标，无论当前目录下是否存在 clean 这个文件，当我们执行 make clean 后 rm 都会被执行。

变量的基本赋值：

-  简单赋值 ( := ) 编程语言中常规理解的赋值方式，只对当前语句的变量有效。
-  递归赋值 ( = ) 赋值语句可能影响多个变量，所有目标变量相关的其他变量都受影响。
-  条件赋值 ( ?= ) 如果变量未定义，则使用符号中的值定义变量。如果该变量已经赋值，则该赋值语句无效。
-  追加赋值 ( += ) 原变量用空格隔开的方式追加一个新值。

特殊符号：

- `-` 符号 (连字符)：任何命令行的任何非零退出状态都被忽略，忽略当前命令行执行时所遇到的错误。

- `@` 符号 (at 符号)：不显示命令本身而只显示结果

- `+` 符号 (加号)：使用加号修饰符让命令始终执行

- `$` 符号 (美元符号)：扩展打开 makefile 中定义的变量

- `$$` 符号：扩展打开 makefile 中定义的 shell 变量
