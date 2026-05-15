

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries -= 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print(reminder)

# 实参按照顺序传递（位置参数)
ask_ok('Do you really want to quit?')
ask_ok('Do you really want to quit?',2)
ask_ok('Do you really want to quit?',2,'请重新输入')
# 实参传递关键字参数必须在位置参数后面
ask_ok('Do you really want to quit?',reminder="请重新输入")
ask_ok('Do you really want to quit?',reminder="请重新输入",retries=2)