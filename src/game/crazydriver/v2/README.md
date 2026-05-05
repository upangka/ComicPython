# 🏎️ 疯狂赛车游戏 v2 - 重构版本

> 一个使用 Python + Pygame 开发的赛车避障游戏，采用面向对象设计和多种设计模式重构。

## 📋 项目概述

这是疯狂赛车游戏的重构版本（v2），从 v1 的过程式代码（137行单文件）重构为模块化、可扩展的面向对象架构（13个文件，约800+行代码）。

### ✨ 核心特性

- 🎮 经典的赛车避障玩法
- 🎯 分数系统和难度递增
- ⏸️ 暂停/继续功能
- 💥 碰撞检测和游戏结束处理
- 🎨 模块化架构，易于扩展

---

## 🏗️ 架构设计

### 文件结构

```
v2/
├── main.py                    # 游戏入口（23行）
├── config.py                  # 配置管理（57行）
├── resources.py               # 资源管理器（90行）
├── game/
│   ├── engine.py              # 游戏引擎核心（239行）
│   └── state.py               # 状态管理系统（172行）
├── entities/                  # 游戏实体
│   ├── base.py                # 实体基类（55行）
│   ├── player.py              # 玩家类（73行）
│   ├── enemy.py               # 敌人类+工厂（121行）
│   └── ui.py                  # UI组件（130行）
├── managers/                  # 管理器
│   ├── collision_manager.py   # 碰撞检测（45行）
│   └── score_manager.py       # 分数管理（41行）
├── images/                    # 图片资源
│   ├── Enemy.png
│   ├── Enemy2.png
│   ├── Enemy3.png
│   ├── Player.png
│   └── Road.png
└── fonts/                     # 字体资源
    └── 字心坊小呀小布丁.TTF
```

### 模块职责

| 模块 | 职责 |
|------|------|
| `GameEngine` | 游戏主循环、协调各组件 |
| `GameStateManager` | 状态切换和管理 |
| `ResourceManager` | 资源加载和缓存 |
| `CollisionManager` | 碰撞检测逻辑 |
| `ScoreManager` | 分数管理 |
| `Player/Enemy` | 各自的行为逻辑 |

---

## 🎨 设计模式应用

### 1. 单例模式 (Singleton)
**位置**: `resources.py` - `ResourceManager`

确保全局只有一个资源管理器实例，避免重复加载资源。

```python
class ResourceManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### 2. 工厂模式 (Factory)
**位置**: `entities/enemy.py` - `EnemyFactory`

封装敌人对象的创建逻辑，便于扩展新敌人类型。

```python
class EnemyFactory:
    @staticmethod
    def create_enemy(enemy_type, resource_manager, screen_width):
        # 根据类型创建不同敌人
        return Enemy(image, position, enemy_type)
```

### 3. 状态模式 (State)
**位置**: `game/state.py`

将不同游戏状态的行为封装到独立类中：
- `RunningState`: 游戏运行中
- `PausedState`: 游戏暂停
- `GameOverState`: 游戏结束

```python
class State(ABC):
    @abstractmethod
    def handle_input(self, keys, game_engine): pass
    
    @abstractmethod
    def update(self, game_engine): pass
    
    @abstractmethod
    def render(self, screen, game_engine): pass
```

### 4. 组合模式 (Composite)
使用 Pygame 内置的 `sprite.Group` 统一管理多个游戏精灵。

### 5. 策略模式 (Strategy)
不同状态类提供不同的 `update()` 和 `render()` 实现，游戏引擎无需关心当前状态的具体行为。

---

## 🐍 Pythonic 特性

### dataclass - 数据类
```python
@dataclass(frozen=True)  # 不可变配置
class GameConfig:
    SCREEN_WIDTH: int = 500
    SCREEN_HEIGHT: int = 800
    COLORS: dict = field(default_factory=lambda: {...})
```

### enum.Enum - 枚举类型
```python
class GameState(Enum):
    RUNNING = "running"
    PAUSED = "paused"
    GAME_OVER = "game_over"
```

### functools.lru_cache - 缓存装饰器
```python
@lru_cache(maxsize=128)
def load_image(self, path: Path) -> pygame.Surface:
    # 自动缓存已加载的图片
```

### abc.ABC - 抽象基类
```python
class BaseEntity(pygame.sprite.Sprite, ABC):
    @abstractmethod
    def update(self, *args, **kwargs): pass
```

### pathlib.Path - 现代路径处理
```python
self.IMAGES_DIR = self._base_dir / 'images'
```

### 完整的类型注解
```python
def check_collision(self) -> bool:
    ...

def render(self, screen: pygame.Surface, game_engine):
    ...
```

---

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Pygame 2.0+

### 安装依赖

```bash
pip install pygame
```

### 运行游戏

```bash
cd D:\Code\CommicPython\Github\ComicPython\src\game\crazydriver\v2
python main.py
```

### 游戏操作

- ⬅️ **左箭头** 或 **A**: 向左移动
- ➡️ **右箭头** 或 **D**: 向右移动
- ⏸️ **空格键**: 暂停/继续游戏
- ❌ **关闭窗口**: 退出游戏

---

## 📊 重构对比

### v1 vs v2

| 指标 | v1（原始） | v2（重构） | 改进 |
|------|-----------|-----------|------|
| **代码行数** | 161行 | ~800行 | 更详细但模块化 |
| **文件数量** | 2个 | 13个 | 职责清晰 |
| **全局变量** | 7个 | 0个 | ✅ 完全消除 |
| **类的数量** | 3个 | 12个 | ✅ 封装完善 |
| **设计模式** | 0个 | 5个 | ✅ 架构优雅 |
| **类型注解** | 无 | 完整 | ✅ 可维护性强 |
| **可扩展性** | 低 | 高 | ✅ 易于添加功能 |
| **可测试性** | 低 | 高 | ✅ 单元可测 |

### 核心优化点

#### 1. 消除全局变量
- ❌ v1: `move_speed`, `score`, `paused` 等全局变量
- ✅ v2: 所有状态封装在类中

#### 2. 资源管理优化
- ❌ v1: 模块级别加载图片，无法复用
- ✅ v2: 单例资源管理器 + LRU缓存

#### 3. 职责分离
每个模块只负责单一功能，符合**单一职责原则 (SRP)**

#### 4. 可扩展性
- ✅ 添加新敌人类型：只需在 `EnemyType` 添加枚举
- ✅ 添加新游戏状态：继承 `State` 类
- ✅ 添加新UI组件：创建新类即可

---

## 🎓 学习要点

### 适合学习的概念

1. **如何识别代码坏味道**
   - 全局变量过多
   - 函数过长
   - 职责混乱

2. **如何选择设计模式**
   - 根据实际问题选择，不为了用而用
   - 模式是解决方案，不是目标

3. **如何渐进式重构**
   - 先拆分文件
   - 再提取类
   - 最后应用设计模式

4. **Python高级特性实战**
   - dataclass、enum、decorator、ABC 的实际应用

### 关键设计原则

- ✅ **单一职责原则 (SRP)**: 每个类只做一件事
- ✅ **开闭原则 (OCP)**: 对扩展开放，对修改关闭
- ✅ **依赖倒置原则 (DIP)**: 依赖抽象而非具体实现

---

## 🔧 已知问题修复

### 1. 初始化顺序问题
**问题**: `_spawn_enemy()` 在 `all_sprites` 创建之前被调用  
**解决**: 调整初始化顺序，先创建精灵组再生成敌人

### 2. 资源管理器缺少路径属性
**问题**: `ResourceManager` 没有 `IMAGES_DIR` 属性  
**解决**: 在 `__init__` 中添加路径属性

### 3. 游戏结束黑屏显示
**问题**: 碰撞后没有显示黑色背景  
**解决**: 在 `render_game_over()` 中填充黑色背景

---

## 🚀 未来扩展方向

### 短期计划
- [ ] 添加道具系统（IceCube、Oil 等障碍物）
- [ ] 多敌人同时生成
- [ ] 音效系统（背景音乐、碰撞音效）

### 中期计划
- [ ] 存档系统（最高分记录）
- [ ] 关卡系统（不同难度的赛道）
- [ ] 粒子效果（碰撞爆炸特效）

### 长期计划
- [ ] 多人模式
- [ ] 在线排行榜
- [ ] 自定义赛道编辑器

> 💡 **提示**: 所有扩展都可以通过新增类实现，无需修改现有代码！

---

## 📝 开发笔记

### 状态流转图

```
[运行中 Running]
      ↓ 按空格
[暂停 Paused]
      ↓ 按空格
[运行中 Running]
      ↓ 碰撞
[游戏结束 GameOver]
      ↓ 5秒后
[退出]
```

### 游戏循环流程

```
1. 处理事件 (Event Handling)
2. 获取当前状态 (Get State)
3. 处理输入 (Handle Input)
4. 更新逻辑 (Update)
5. 渲染画面 (Render)
6. 刷新显示 (Flip Display)
```

---

## 📄 许可证

本项目仅供学习和参考使用。

---

## 🙏 致谢

- Pygame 社区提供的优秀游戏开发框架
- 设计模式相关书籍和资料
- Python 官方文档

---

**Happy Coding! 🎮✨**
