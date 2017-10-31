#  --*-coding:utf-8-*--

import unittest

class TestClass(unittest.TestCase):
    def test_01(self):
        """ Pythonにおける「クラス変数」の扱いの確認
        """

        class Foo(object):
            X = 10

        foo = Foo()
        self.assertEqual(Foo.X, 10)
        self.assertEqual(foo.X, 10)

        Foo.X = 20
        self.assertEqual(Foo.X, 20)
        self.assertEqual(foo.X, 20)
        
        foo.X = 30
        self.assertEqual(Foo.X, 20)
        self.assertEqual(foo.X, 30)

        Foo.X = 40
        self.assertEqual(Foo.X, 40)
        self.assertEqual(foo.X, 30)


if __name__ == '__main__':
    unittest.main()
