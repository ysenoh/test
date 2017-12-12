#  --*-coding:utf-8-*--

import time
import itertools

N = 1000000

def test1():
    a = list(range(N))

    t0 = time.time()
    b = a[1:]
    for i in range(100):
        sum(b)

    t1 = time.time()
    print(t1 - t0)


def test2():
    a = list(range(N))

    t0 = time.time()
    for i in range(100):
        sum(a[1:])

    t1 = time.time()
    print(t1 - t0)


def test3():
    a = list(range(N))
    assert sum(itertools.islice(a, 1, len(a))) == N*(N-1)//2

    t0 = time.time()
    for i in range(100):
        sum(itertools.islice(a, 1, len(a)))

    t1 = time.time()
    print(t1 - t0)


def test4():
    a = list(range(N))

    t0 = time.time()
    for i in range(100):
        b = (a[j] for j in range(1, len(a)))
        sum(b)

    t1 = time.time()
    print(t1 - t0)


test1() 
test2() # 毎回配列をコピーしているので遅い
test3() # イテレータとして配列をコピーしないので、少し速い
test4() # イテレータとして配列をコピーしないが、これだととても遅い
