"""基本計算模組"""


def divide(a, b):
    """
    計算兩數相除的結果

    參數：
        a (int | float): 被除數
        b (int | float): 除數，不可為 0

    回傳：
        float: a 除以 b 的商

    例外：
        ValueError: 當除數 b 為 0 時拋出
    """
    if b == 0:  # 檢查除數是否為 0（包含整數 0 與浮點數 0.0）
        raise ValueError("除數不可為零")
    return a / b  # 回傳一般除法結果
