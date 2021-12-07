"""标准库tracemalloc 跟踪内存分配"""
import tracemalloc

# 开始跟踪内存分配
tracemalloc.start()

a = list(range(100000))
b = list(range(10))

# 快照，当前内存分配
snapshot = tracemalloc.take_snapshot()

# 快照对象的统计
top_stats = snapshot.statistics('lineno')

# 查看总内存使用
stats = snapshot.statistics('filename')

print("[ Top 10 ]")
for stat in stats[:10]:
    print(stat)
