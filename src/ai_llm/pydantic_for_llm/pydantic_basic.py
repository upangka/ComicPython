from typing import Optional
from pydantic import BaseModel, EmailStr


class UserInput(BaseModel):
    name: str
    email: EmailStr
    query: str
    age: Optional[int] = None


user_input = UserInput(
    name="Pkmer",
    email="pkmer@example.com",
    query="Happy Coding",
    age="20"
)


print(user_input)
import inspect
# 打印为UserInput生成的构造方法签名
print(inspect.signature(UserInput))
print(inspect.signature(UserInput.__init__))