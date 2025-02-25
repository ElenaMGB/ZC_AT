import unittest
from main_01 import divide_rest

class TestDivideRest(unittest.TestCase):
    def test_divide_r_success(self):
        self.assertEqual(divide_rest(10, 4), 2)
        self.assertEqual(divide_rest(22, 7), 1)
        self.assertEqual(divide_rest(35, 3), 2)

    def test_divide_r_by_zero_1(self): #тест с параметрами. Подходит для простых случаев, когда нужно проверить вызов одной функции
        self.assertRaises(ValueError, divide_rest, 6, 0)

    def test_divide_r_by_zero_2(self): #тест с конструкцией with. позволяет проверять, что любой код внутри блока with вызывает исключение ValueError
        with self.assertRaises(ValueError):
            divide_rest(6, 0)

if __name__ == '__main__':
		unittest.main()
