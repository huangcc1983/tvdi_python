"""calc 模組的單元測試"""

import unittest
from calc import divide


class TestCalc(unittest.TestCase):
    """測試 calc.py 中的計算函式"""

    def test_divide_normal(self):
        """測試一般正數除法"""
        self.assertEqual(divide(10, 2), 5.0)  # 整除情況
        self.assertEqual(divide(7, 2), 3.5)  # 帶有小數的情況

    def test_divide_negative_and_zero_numerator(self):
        """測試負數與被除數為 0 的除法"""
        self.assertEqual(divide(-9, 3), -3.0)  # 負數除以正數
        self.assertEqual(divide(0, 5), 0.0)  # 被除數為 0 時商為 0

    def test_divide_by_zero(self):
        """測試除數為整數 0 時拋出 ValueError"""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "除數不可為零")

    def test_divide_by_zero_float(self):
        """測試除數為浮點數 0.0 時拋出 ValueError"""
        with self.assertRaises(ValueError) as context:
            divide(10, 0.0)
        self.assertEqual(str(context.exception), "除數不可為零")


if __name__ == "__main__":
    unittest.main()
