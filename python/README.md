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

イテレータにすれば良いのかと思って、(a[i] for i in rage(1, len(a))) の様に書いたところ却って遅かった。(test03.test4)  
やはり単純に配列としてアクセスすると遅い。  

+ サンプルコード: [test03.py](test03.py)




# <a name="TEST04">TEST04: importの実行
importは関数内でも実行できる。  
その名前の解決は、その関数内でのみ有効である。  
その関数から呼び出している関数内では使用できない。  

2回importしてもステートメントは1回しか実行されない。  
異なる関数内で呼び出した場合もそう。  
 
+ サンプルコード: [test04.py](test04.py) [test04sub.py](test04sub.py)


# <a name="TEST05">TEST05: 引数のデフォルト値が決定されるタイミング
引数のデフォルト値が変数で与えられている場合、その変数が変更されたらどうなるのか。  
テストしてみた範囲では、どうも関数が定義されるタイミングで、その変数の値(インスタンス)が設定されるらしい。  

つまり、関数定義より後に変数の値を変更しても反映されない。  
オブジェクトであっても、変数に上書きした場合は同様。  
ただし、変数ではなく、そのインスタンス自身を更新した場合は、それが反映される。  
 
+ サンプルコード: [test05.py](test05.py)

