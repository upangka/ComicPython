# Python 内置模块练习目录

本目录用于存放 Python 内置模块（标准库）的练习代码。

## 📁 目录结构规划

```
builtin_modules/
├── functools/
│   ├── cache_demo.py          # @cache, @lru_cache 演示
│   ├── partial_demo.py        # partial 函数应用
│   ├── reduce_demo.py         # reduce 使用示例
│   └── wraps_demo.py          # @wraps 装饰器
│
├── itertools/
│   ├── infinite_iterators.py  # count, cycle, repeat
│   ├── combinatorics.py       # permutations, combinations
│   ├── grouping.py            # groupby 使用
│   └── chaining.py            # chain, tee 等
│
├── collections/
│   ├── counter_demo.py        # Counter 计数器
│   ├── defaultdict_demo.py    # defaultdict 使用
│   ├── namedtuple_demo.py     # namedtuple 命名元组
│   └── deque_demo.py          # deque 双端队列
│
├── contextlib/
│   ├── context_manager.py     # 上下文管理器
│   └── suppress_demo.py       # suppress 异常抑制
│
├── pathlib/
│   ├── path_operations.py     # 路径操作
│   └── file_operations.py     # 文件操作
│
├── datetime_module/
│   ├── date_basics.py         # date 对象
│   ├── time_basics.py         # time 对象
│   └── timedelta_calc.py      # 时间计算
│
├── typing_module/
│   ├── type_hints.py          # 类型提示基础
│   └── generics.py            # 泛型使用
│
├── re_module/
│   ├── basic_patterns.py      # 基础正则表达式
│   └── advanced_matching.py   # 高级匹配
│
└── README.md                  # 本说明文档
```

## 📝 使用说明

- 每个子目录对应一个 Python 内置模块
- 每个文件专注于该模块的特定功能或特性
- 文件名采用描述性命名，便于快速定位学习内容
- 建议在学习新模块时，先创建对应的子目录和练习文件

## 🎯 学习目标

通过系统的练习，掌握 Python 常用内置模块的使用方法和最佳实践。
