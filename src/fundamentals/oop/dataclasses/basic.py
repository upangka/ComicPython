from dataclasses import dataclass,fields
import inspect

@dataclass
class User:
    # 对象特性
    name: str
    age: int = 18

    # 类特性 共享的
    email = "pkmer@py.cn"


print(inspect.signature(User))

from dataclasses import fields
for field in fields(User):
    print(f"字段 {field.name}: 默认值 = {field.default}")

print({k:v for k, v in User.__dict__.items() if not k.startswith('_')})