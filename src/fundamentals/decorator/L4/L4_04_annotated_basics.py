"""
Annotated 注解的基础使用和理解

本模块展示了 typing.Annotated 的基本用法。Annotated 允许在类型注解中
附加元数据，这些元数据不会影响类型检查，但可以被运行时库读取和使用。
常用于依赖注入、验证、序列化等场景，是 Python 3.9+ 的重要特性。
"""
import functools
from typing import Annotated, get_type_hints

def happy_birthday(name: Annotated[str, ("在深圳", 18), "希望你天天开心"],
                   age,
                   address,
                   msg) -> str:
    """通过获取Annotated里面的元数据类进行赋值"""
    if age and address and msg:
        print(f"🎂 祝 {name} {age}岁生日快乐！你现在在{address}，{msg}")
    else:
        print("happy_birthday", name, age, address, msg)
    print(f"祝福已发送给 {name}")


# {'name': typing.Annotated[str, ('在深圳', 18), '希望你天天开心'], 'return': <class 'str'>}
hints = get_type_hints(happy_birthday, include_extras=True)

for name, annotation in hints.items():
    # 获取Annotated类型注解
    if hasattr(annotation, "__metadata__"):
        (address, age), msg = getattr(annotation, "__metadata__")
        happy_birthday = functools.partial(happy_birthday, age=age, address=address, msg=msg)

happy_birthday("Pkmer")

"""
🎂 祝 Pkmer 18岁生日快乐！你现在在在深圳，希望你天天开心
祝福已发送给 Pkmer
"""
