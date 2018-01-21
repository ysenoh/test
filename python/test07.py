#  --*-coding:utf-8-*--

import unittest

class TestInherit(unittest.TestCase):
    def test_01(self):
        class Foo(object):
            def func(self):
                return('Foo.func')

            def _func(self):
                return('Foo._func')

            def __func(self):
                return('Foo.__func')

            def test(self):
                return [self.func(),
                        self._func(),
                        self.__func()]


        class Boo(Foo):
            def func(self):
                return('Boo.func')

            def _func(self):
                return('Boo._func')

            def __func(self):
                return('Boo.__func')


        x = Boo()
        y = x.test()

        self.assertEqual(y[0], 'Boo.func')
        self.assertEqual(y[1], 'Boo._func')
        self.assertEqual(y[2], 'Foo.__func')


if __name__ == '__main__':
    unittest.main()




