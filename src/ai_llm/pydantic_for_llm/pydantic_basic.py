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


def create_user():
    user_input = UserInput(
        name="Pkmer",
        email="pkmer@example.com",
        query="Happy Coding",
    )
    print(user_input.model_dump_json(indent=2))


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
    """验证用户输入数据并创建 UserInput 实例。

    使用 Pydantic 模型对用户输入进行校验，如果校验成功则打印格式化的 JSON 数据，
    如果校验失败则打印错误信息并抛出 ValidationError 异常。

    Args:
        user_input: 包含用户输入数据的字典，必须包含 name、email、query 字段，
                   purchase 和 order_id 字段为可选。

    Raises:
        ValidationError: 当输入数据不符合 UserInput 模型的校验规则时抛出。

    Examples:

        正确案例 - 校验成功：

        >>> input_data = {
        ...     "name": "Pkmer",
        ...     "email": "Pkmer@example.com",
        ...     "query": "Happy Coding",
        ...     "purchase": "2026-05-08"
        ... }
        >>> validate_user_input(input_data)
        ✅ Valid user input created:
        {
          "name": "Pkmer",
          "email": "Pkmer@example.com",
          "query": "Happy Coding",
          "purchase": "2026-05-08",
          "order_id": null
        }

        错误案例 - 校验失败（order_id 不满足约束）：

        >>> invalid_data = {
        ...     "name": "Pkmer",
        ...     "email": "Pkmer@example.com",
        ...     "query": "Happy Coding",
        ...     "purchase": "2026-05-08",
        ...     "order_id": "125"
        ... }
        >>> validate_user_input(invalid_data)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ❌ Validation error occurred:
        - order_id: Input should be greater than or equal to 10000
    """
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


def json_str_to_model_v1():
    """将 JSON 字符串转换为 UserInput 模型实例。"""
    json_data = '''
        {
            "name": "Pkmer",
            "email": "Pkmer@example.com",
            "query": "Happy Coding",
            "order_id": "12345",
            "purchase": "2026-05-08"
        }
        '''
    import json
    input_data = json.loads(json_data)
    print(type(input_data)) # <class 'dict'>
    user_input = UserInput(**input_data)
    print(user_input)
    print(user_input.model_dump_json(indent=2))


def json_str_to_model_v2():
    """将 JSON 字符串转换为 UserInput 模型实例。"""
    json_data = '''
        {
            "name": "Pkmer",
            "email": "Pkmer@example.com",
            "query": "Happy Coding",
            "order_id": "12345",
            "purchase": "2026-05-08"
        }
        '''
    user_input = UserInput.model_validate_json(json_data)
    print(user_input)
    print(user_input.model_dump_json(indent=2))

if __name__ == '__main__':
    json_str_to_model_v2()