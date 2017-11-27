# 概要
JavaScriptの動作に関する簡単なテストコード。  
単に不勉強だっただけで、大したことは書いてない。  

# TEST01: グローバルな変数の扱い
JavaScriptにおいて、グローバルな変数は、windowオブジェクトの属性値として扱われるので、
例えば closed の様な名前の変数は定義できない。  
エラーにもならない。

+ サンプルコード: [test01.html](test01.html)
+ windowオブジェクトのプロパティ一覧: [test01_properties.txt](test01_properties.txt)


# TEST02: styleの変更とイベントハンドラの呼出タイミング
以前、Edgeでは以下の動作をしていたはずなので、その確認をした。  
多分、手順は間違っていないと思うが、再現しなかった。  
バグとして修正されたのだと思う。  

1. focusされているinputタグが存在している。
1. そのタグを含むdivタグのstyle.display属性に noneを設定する。
1. その設定処理が完了する前にonBlurイベントハンドラが呼び出される。

+ サンプルコード: [test02.html](test02.html)
