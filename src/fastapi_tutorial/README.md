```shell
uv add "fastapi[standard-no-fastapi-cloud-cli]"
```

```txt
fastapi_tutorial/
├── .gitignore
├── pyproject.toml
├── uv.lock
│
├── stage_01_quickstart/          # 阶段1：快速入门
│   ├── step_01_hello_world/      #   步骤1：第一个API
│   │   └── main.py
│   ├── step_02_path_params/      #   步骤2：路径参数
│   │   └── main.py
│   ├── step_03_query_params/     #   步骤3：查询参数
│   │   └── main.py
│   └── step_04_request_body/     #   步骤4：请求体
│       └── main.py
│
├── stage_02_pydantic_models/     # 阶段2：数据模型与校验
│   ├── step_01_basic_models/
│   │   └── main.py
│   ├── step_02_nested_models/
│   │   └── main.py
│   ├── step_03_field_validator/
│   │   └── main.py
│   └── step_04_response_model/
│       └── main.py
│
├── stage_03_dependency_injection/ # 阶段3：依赖注入
│   ├── step_01_simple_deps/
│   │   └── main.py
│   ├── step_02_deps_with_params/
│   │   └── main.py
│   └── step_03_class_deps/
│       └── main.py
│
├── stage_04_database/            # 阶段4：数据库集成
│   ├── step_01_sqlalchemy_setup/
│   │   └── main.py
│   ├── step_02_crud_operations/
│   │   └── main.py
│   └── step_03_relationships/
│       └── main.py
│
├── stage_05_auth/                # 阶段5：认证与授权
│   ├── step_01_jwt_auth/
│   │   └── main.py
│   └── step_02_oauth2/
│       └── main.py
│
└── stage_06_advanced/            # 阶段6：进阶主题
    ├── step_01_middleware/
    │   └── main.py
    ├── step_02_background_tasks/
    │   └── main.py
    └── step_03_websocket/
        └── main.py
```
