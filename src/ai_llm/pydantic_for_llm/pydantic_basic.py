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

def create_user():
    print(user_input)

def inspect_user_input():
    """打印为UserInput生成的构造方法签名"""
    import inspect
    print(inspect.signature(UserInput))
    print(inspect.signature(UserInput.__init__))


def json_schema():
    """查看json_schema"""
    from pprint import pprint
    pprint(UserInput.model_json_schema())


def validate_user_input():
    """数据校验"""
    UserInput(
        name="Pkmer",
        email="not-an-email",  # 非法的邮箱
        query="Happy Coding古法编程之美"
    )


