"""
演示Python中仅位置参数（Positional-Only Parameters）的使用方法
"""

def func(pos1, pos2, /, pos_or_kw1, pos_or_kw2, *, kw1, kw2):
    """
    pos1, pos2          → 仅位置（/ 左边）
    pos_or_kw1, pos_or_kw2 → 位置或关键字（/ 和 * 之间）
    kw1, kw2            → 仅关键字（* 右边）
    """
    pass

# 合法调用
func(1, 2, 3, 4, kw1=5, kw2=6)        # ✅
func(1, 2, 3, pos_or_kw2=4, kw1=5, kw2=6)  # ✅
print(func.__code__.co_posonlyargcount) # 2
print(func.__code__.co_kwonlyargcount) # 2
print(func.__code__.co_varnames) #  ('pos1', 'pos2', 'pos_or_kw1', 'pos_or_kw2', 'kw1', 'kw2')
# 非法调用
# func(pos1=1, pos2=2, ...)  # ❌ TypeError: got positional-only arguments as keyword


def func_name(name,/,**kwargs):
    print(f"{name=} \n{kwargs=}")

# 注意这里关键字传递实参 name="深圳图书馆"，并没有影响前面位置参数 name
func_name("Pkmer",name="深圳图书馆")
"""输出
name='Pkmer' 
kwargs={'name': '深圳图书馆'}
"""
# 仅位置参数数量
print(func_name.__code__.co_posonlyargcount) # 1
