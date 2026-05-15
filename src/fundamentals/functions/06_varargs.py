"""
演示Python中可变数量位置形参（*args）的使用方法
"""


def concat(city="深圳", *args, sep="/"):
    print(f"{type(args) = } {args=}")
    return sep.join((city,) + args)


print(concat("北京", "上海", "广州", sep=" | "))
print(concat())


def query_data(table, limit=0, offset=20):
    print(f"select from {table} limit {limit, offset}")


query_data("user")


def wrapper(*args, **kwargs):
    print(f"{args=} {kwargs=}")
    query_data(*args, **kwargs)  # 无透明传递
    print("-"*45)


wrapper("user", limit=10, offset=20)
wrapper("user", 10, 20)
wrapper(**{"table": "user", "limit": 10, "offset": 20})
