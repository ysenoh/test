#  --*-coding:utf-8-*--

DEFAULT_VAL = 10

def f(x=DEFAULT_VAL):
    print(x)

DEFAULT_VAL = 20

f() # 10が表示される


class Foo(object):
    def __init__(self, n):
        self.n = n

foo = Foo(10)

def g(x=foo):
    print(x.n)

foo = Foo(20)

g() # 10が表示される


def h(x=foo):
    print(x.n)
    

foo.n = 30
h() # 30が表示される
