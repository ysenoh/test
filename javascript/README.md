# 概要
JavaScriptの動作に関する簡単なテストコード。  
単に不勉強だっただけで、大したことは書いてない。  

# TEST01: グローバルな変数の扱い
JavaScriptにおいて、グローバルな変数は、windowオブジェクトの属性値として扱われるので、
例えば closed の様な名前の変数は定義できない。  
エラーにもならない。

+ サンプルコード: [test01.html](test01.html)


# TEST02: styleの変更とイベントハンドラの呼出タイミング
以前、Edgeでは以下の動作をしていたはずなので、その確認をした。  
多分、手順は間違っていないと思うが、再現しなかった。  
バグとして修正されたのだと思う。  

1. focusされているinputタグが存在している。
1. そのタグを含むdivタグのstyle.display属性に noneを設定する。
1. その設定処理が完了する前にonBlurイベントハンドラが呼び出される。

+ サンプルコード: [test02.html](test02.html)


# TEST03: 値を変更できないプロパティ
Object.defineProperties でプロパティのwritableディスクリプタにfalseを設定すると、そのプロパティは値を変更できない。  
また、prototypeに対して同様な設定をしたプロパティを設定すると、そのprototype に対してだけでなく、オブジェクトの属性値としても値を変更できない。  
値を代入してもエラーも出ないので、非常に危うい。  

このディスクリプタにはwritable以外にも色々ある。  
[MDN: Object.defineProperties()](https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Object/defineProperties)

+ サンプルコード: [test03.js](test03.js)
