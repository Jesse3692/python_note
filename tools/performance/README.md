# 性能分析

## KCachegrind

```shell
# 为访问剖析信息，首先需要生成 cProfile 输出文件。
python -m cProfile -o prof.out taylor.py 
# 然后，就可使用 pyprof2calltree 对输出文件进行转换并启动 KCachegrind。
pyprof2calltree -i prof.out -o prof.calltree 
kcachegrind prof.calltree # 或使用命令 qcachegrind prof.calltree 
```
