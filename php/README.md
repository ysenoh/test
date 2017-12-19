# 概要
PHPの動作に関する簡単なテスト。  
大したことは書いてない。  
正しいかどうかも良くわからない。  

# <a name="TEST01">TEST01: finally からthrow
tryブロック内で例外が発生している状態で、finally でthrowした場合は、finally 内の例外がthrowされる。  
その例外には、tryブロック内で発生した例外が、previousとして設定されている。  

+ [PHPリファレンスマニュアル Exception::getPrevious](http://php.net/manual/ja/exception.getprevious.php)
+ テストコード(test01.php)


