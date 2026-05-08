from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, ValidationError, Field


class UserInput(BaseModel):
    name: str
    email: EmailStr
    query: str
    purchase: Optional[date] = None
    order_id: Optional[int] = Field(
        None,
        title="订单ID",
        description="5 位订单号（不能以 0 开头）",
        ge=10000,
        le=99999
    )


def create_user(user_input):
    user_input = UserInput(
        name="Pkmer",
        email="pkmer@example.com",
        query="Happy Coding",
        age="20"
    )
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


def error_validate_demo():
    """查看数据校验"""
    UserInput(
        name="Pkmer",
        email="not-an-email",  # 非法的邮箱
        query="Happy Coding古法编程之美"
    )


def validate_user_input(user_input: dict):
    try:
        user_input = UserInput(**user_input)
        print(f"✅ Valid user input created:")
        print(f"{user_input.model_dump_json(indent=2)}")
    except ValidationError as e:
        print(f"❌ Validation error occurred:")
        for error in e.errors():
            print(f"- {error['loc'][0]}: {error['msg']}")
            # print(error)
        raise


if __name__ == '__main__':
    input_data = {
        "name": "Pkmer",
        "email": "Pkmer@example.com",
        "query": "Happy Coding",
        "purchase": "2026-05-08",
        "order_id": "666",
    }
    validate_user_input(input_data)
