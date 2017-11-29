var obj = new Object();
Object.defineProperty(
    obj, 'x',
    {value: 10, writable: false});

obj.x = 20;
console.log(obj.x); // 10が出力される


function Foo() {
}

Object.defineProperty(
    Foo.prototype, 'x',
    {value: 10, writable: false});

var foo = new Foo();
foo.x = 20;
console.log(foo.x); // 10が出力される
