# 概要
Python3の動作に関する簡単なテスト。  
大したことは書いてない。  
正しいかどうかも良くわからない。  

# TEST01: Pythonのクラス変数
Pythonでもクラス変数は定義できる。  
それはインスタンスの変数としても参照できる。  
ただし、インスタンスの変数として代入すると、別の変数として管理される。  
globalと同じようなスコープで管理されているっぽい。  

+ サンプルコード: [test_class.py](test_class.py)

# TEST02: Pythonのマルチバイト文字のstdout出力
以下の設定をするのが簡単な様である。
```
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```

sys.stdout は　io.TextIOWrapper のインスタンスであり、
これは io.TextIOBase を継承している。  
bufferは、根底のバイナリバッファである、 io.BufferedIOBase のインスタンスである。  

+ サンプルコード: [encoding.py](encoding.py)

# <a name="TEST03">TEST03: 配列の切り出しのコスト
pythonで a[1:] の様な操作をした場合のコストが気になったので、簡単に調査。  
やはりこれは配列のコピー操作なので、ちょっと重い。  
気になる場合は、[itertools.islice](https://docs.python.jp/3/library/itertools.html#itertools.islice)を使うと、イテレータとして処理できるらしい。  

+ サンプルコード: [test03.py](test03.py)
