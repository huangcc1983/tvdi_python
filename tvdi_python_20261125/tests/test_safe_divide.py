"""safe_divide_demo 模組的單元測試"""

import unittest
from safe_divide_demo import safe_divide


class TestSafeDivide(unittest.TestCase):
    """測試 safe_divide_demo.py 中的安全除法函式"""

    def test_safe_divide_normal(self):
        """測試一般正數安全除法"""
        self.assertEqual(safe_divide(10, 2), 5.0)
        self.assertEqual(safe_divide(7, 2), 3.5)

    def test_safe_divide_by_zero_returns_none(self):
        """測試除數為 0 時捕捉 ValueError 並回傳 None"""
        self.assertIsNone(safe_divide(10, 0))
        self.assertIsNone(safe_divide(10, 0.0))

    def test_safe_divide_invalid_type_returns_none(self):
        """測試傳入非數字型別時捕捉 TypeError 並回傳 None"""
        self.assertIsNone(safe_divide("10", 2))
        self.assertIsNone(safe_divide(10, "2"))


if __name__ == "__main__":
    unittest.main()
