x = 0
y = 0
act = ''


def init(a, b, action):
    global x, y, act
    #global y
    #global act
    x = a
    y = b
    act = action


def do_it():
    if act == '+':
        return x + y
    if act == '-':
        return x - y
    if act == '*':
        return x * y
    if act == '/':
        return x / y
       