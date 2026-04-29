# 项目开发规则

## 开发环境

- **Python 版本**: 3.13
- **操作系统**: Windows 22H2
- **Shell**: PowerShell

## 代码规范

### Python 代码风格
- 遵循 PEP 8 编码规范
- 使用 4 空格缩进
- 最大行长度: 88 字符（推荐）或 120 字符（可选）
- 使用有意义的变量和函数命名（snake_case）
- 类名使用 PascalCase

### 文档与注释
- 所有公共模块、类和函数需要添加 docstring
- 使用中文注释解释复杂逻辑
- 关键算法和业务逻辑必须添加说明注释

### 类型提示
- 优先使用类型注解（Type Hints）
- 导入 `typing` 模块中的类型工具
- 函数参数和返回值应明确标注类型

## 项目管理

### 依赖管理
- 使用 `requirements.txt` 或 `pyproject.toml` 管理依赖
- 记录所有第三方库及其版本号
- 定期更新依赖并测试兼容性

### 文件组织
- 模块化设计，单一职责原则
- 合理的目录结构分离关注点
- 避免循环导入

## Git 规范

### 提交信息
- 使用清晰的提交信息描述变更内容
- 格式: `<type>: <description>`
- 类型包括: feat, fix, docs, style, refactor, test, chore

### 分支策略
- 主分支: `main` 或 `master`
- 功能分支: `feature/<feature-name>`
- 修复分支: `fix/<issue-description>`

---

> **说明**: 本规则文件会随着项目发展持续完善，新增规则请按类别添加到相应章节。