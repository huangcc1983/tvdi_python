"""示範使用 try ~ except 搭配 calc.py 進行安全除法運算"""

from calc import divide


def safe_divide(numerator, denominator):
    """
    安全執行兩數相除，遇到型別錯誤或除數為 0 時不讓程式中斷

    參數：
        numerator (int | float): 被除數
        denominator (int | float): 除數

    回傳：
        float | None: 計算成功時回傳商；發生錯誤時回傳 None
    """
    try:
        result = divide(numerator, denominator)
    except ValueError as error:
        print(f"計算失敗（數值錯誤）：{error}")
        return None
    except TypeError:
        print("計算失敗（型別錯誤）：被除數與除數都必須是數字。")
        return None
    else:
        print(f"計算成功：{numerator} / {denominator} = {result}")
        return result


if __name__ == "__main__":
    safe_divide(10, 2)
    safe_divide(10, 0)
    safe_divide("10", 2)
