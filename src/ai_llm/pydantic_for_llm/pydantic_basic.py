from typing import Optional
from xml.etree.ElementTree import indent

from pydantic import BaseModel, EmailStr, ValidationError


class UserInput(BaseModel):
    name: str
    email: EmailStr
    query: str
    age: Optional[int] = None



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
    """验证用户输入数据并创建 UserInput 实例。

    使用 Pydantic 模型对用户输入进行校验，如果校验成功则打印格式化的 JSON 数据，
    如果校验失败则打印错误信息并抛出 ValidationError 异常。

    Args:
        user_input: 包含用户输入数据的字典，必须包含 name、email、query 字段，
                   age 字段为可选。

    Raises:
        ValidationError: 当输入数据不符合 UserInput 模型的校验规则时抛出。

    Examples:
        >>> input_data = {
        ...     "name": "Pkmer",
        ...     "email": "Pkmer@example.com",
        ...     "query": "Happy Coding"
        ... }
        >>> validate_user_input(input_data)
        ✅ Valid user input created:
        {
          "name": "Pkmer",
          "email": "Pkmer@example.com",
          "query": "Happy Coding",
          "age": null
        }
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


if __name__ == '__main__':
    input_data = {
        "name": "Pkmer",
        "email": "Pkmer@example.com",
        "query": "Happy Coding"
    }
    validate_user_input(input_data)