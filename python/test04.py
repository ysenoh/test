#  --*-coding:utf-8-*--

def f1():
    print("f1")
    import test04sub # import のスクリプトが実行される
    test04sub.g() # 呼び出せる　
    f1Sub()

def f1Sub():
    print("f1Sub")
    # test04sub.g() # エラーになる

def f2():
    print("f2")
    import test04sub # import のスクリプトは実行されない
    test04sub.g() # 呼び出せる　

f1()
f2()

# test04sub.g() # エラーになる
