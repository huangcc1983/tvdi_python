# Python 基礎程式實作期末報告：三個大綱方向指南

本文件專為 **Python 初學者個人實作專題**所設計，提供三個不同類型的期末報告大綱方向（生活工具類、資料管理類、互動遊戲類）。每個方向都先說明「為什麼選這個題目」，再整理完整的「報告章節架構」，並附上**可直接執行的核心範例程式碼**，方便您快速挑選主題並著手開發。

---

## 目錄

1. [三個大綱方向總覽比較表](#1-三個大綱方向總覽比較表)
2. [方向一：個人日常記帳小幫手（生活實用工具類）](#2-方向一個人日常記帳小幫手生活實用工具類)
3. [方向二：學員成績管理與統計系統（資料管理統計類）](#3-方向二學員成績管理與統計系統資料管理統計類)
4. [方向三：終極密碼闖關小遊戲（互動娛樂邏輯類）](#4-方向三終極密碼闖關小遊戲互動娛樂邏輯類)
5. [個人期末專題執行 5 步驟建議](#5-個人期末專題執行-5-步驟建議)
6. [重點整理](#6-重點整理)

---

## 1. 三個大綱方向總覽比較表

在決定題目前，可以先透過下表比較三個方向在難度、練習到的 Python 語法與展示效果上的差異：

| 比較項目 | 方向一：個人日常記帳小幫手 | 方向二：學員成績管理與統計系統 | 方向三：終極密碼闖關小遊戲 |
| :--- | :--- | :--- | :--- |
| **主題定位** | 生活實用工具類 | 資料管理與統計類 | 互動娛樂邏輯類 |
| **實作難度** | ★★☆☆☆（入門友善） | ★★★☆☆（結構清楚） | ★★☆☆☆（邏輯直覺） |
| **核心 Python 語法** | 函式（`def`）、串列（`list`）、字典（`dict`）、例外處理（`try / except`） | 條件判斷（`if / elif / else`）、迴圈（`for`）、統計運算、防呆驗證 | 亂數模組（`random`）、迴圈（`while`）、範圍判斷、計數器 |
| **報告展示亮點** | 貼近日常生活，容易展示「輸入錯誤金額不會當機」的防呆設計 | 報表條理分明，能同時呈現平均分數、最高最低分與等第分布 | 上台 Demo（實際操作展示）氣氛最生動，互動感最強 |
| **適合對象** | 喜歡做出「自己平常真的能用」工具的學員 | 喜歡表格統計、邏輯嚴謹、未來想往資料處理發展的學員 | 喜歡遊戲互動、想練習流程控制與條件判斷的學員 |
| **進階加分方向** | 將記帳紀錄存成 `.txt` 或 `.csv` 文字檔（後續課程主題） | 匯出班級成績單報表或依分數排序顯示 | 加入難度選擇（簡單／困難）與猜測次數排行榜 |

---

## 2. 方向一：個人日常記帳小幫手（生活實用工具類）

### 一、為什麼選擇這個方向？（設計目的）

許多人每天都會買飲料、搭車或吃三餐，但常常月底才發現錢不知道花去哪裡。透過 Python 製作一個簡易的「文字版記帳小幫手」，能把課堂學過的**函式（Function，將重複工作打包的功能區塊）**與**例外處理（`try / except`，預防程式因錯誤輸入而當機的保護機制）**實際應用在生活中。

### 二、建議期末報告章節大綱

1. **研究背景與動機**
   - 說明日常零碎花費難以統計的痛點。
   - 說明開發文字版記帳工具的目的（練習資料儲存與輸入檢查）。
2. **系統功能設計與操作流程**
   - 主選單設計：1. 新增消費紀錄、2. 查看所有明細、3. 計算總金額與分類統計、4. 離開程式。
   - 繪製簡單的操作流程圖（開始 ➔ 顯示選單 ➔ 執行功能 ➔ 回到選單）。
3. **核心程式架構與設計邏輯**
   - 說明如何用串列（`list`，像清單一樣依序存放多筆資料的容器）存放多筆花費。
   - 說明如何用字典（`dict`，以「名稱：數值」配對存放單筆資料的容器）記錄項目、分類與金額。
   - 說明每個自訂函式的分工（例如：`add_expense` 負責新增、`calculate_total` 負責加總）。
4. **防呆與例外處理測試**
   - 測試使用者輸入非數字（如 `"abc"`）或負數金額時，程式如何透過 `try / except`（例外處理）提示錯誤而不閃退。
5. **成果展示與學習心得**
   - 附上終端機（Terminal，執行文字指令的視窗）執行畫面截圖。
   - 分享開發過程遇到的困難、解決方式，以及未來想擴充的存檔功能（此部分進階檔案讀寫會在後續課程深入介紹）。

### 三、核心範例程式碼（可直接執行）

以下範例示範如何新增消費、使用 `try / except` 阻擋錯誤金額，並計算總花費：

```python
DEFAULT_CATEGORY = "其他"  # 預設消費分類常數


def add_expense(expense_list, item_name, raw_amount, category=DEFAULT_CATEGORY):
    """
    新增一筆消費紀錄至記帳清單中，並驗證金額是否合法

    參數：
        expense_list (list): 存放所有消費紀錄的串列
        item_name (str): 消費項目名稱
        raw_amount (str | int | float): 使用者輸入的原始金額資料
        category (str): 消費分類，預設為「其他」

    回傳：
        bool: 新增成功回傳 True，格式或金額不合法回傳 False
    """
    try:
        amount = int(raw_amount)  # 嘗試將輸入轉換為整數
        if amount <= 0:
            print(f"新增失敗：「{item_name}」的金額必須大於 0 元。")
            return False
    except ValueError:
        # 當輸入文字無法轉成整數時，捕捉 ValueError（數值錯誤）避免程式當機
        print(f"新增失敗：「{raw_amount}」不是有效的整數金額，請重新輸入數字。")
        return False

    record = {
        "項目": item_name,
        "分類": category,
        "金額": amount,
    }
    expense_list.append(record)
    print(f"已記錄：{item_name}（{category}）{amount} 元")
    return True


def calculate_total(expense_list):
    """
    計算記帳清單中所有消費的總金額

    參數：
        expense_list (list): 存放消費紀錄字典的串列

    回傳：
        int: 總花費金額
    """
    total = 0
    for record in expense_list:
        total += record["金額"]
    return total


if __name__ == "__main__":
    my_expenses = []  # 建立空的記帳清單

    # 測試正常輸入與錯誤輸入的防呆效果
    add_expense(my_expenses, "珍珠奶茶", "65", "飲料")
    add_expense(my_expenses, "雞腿便當", "110", "餐飲")
    add_expense(my_expenses, "公車車資", "abc", "交通")  # 刻意測試文字錯誤
    add_expense(my_expenses, "餅乾", "-20", "零食")      # 刻意測試負數金額

    total_spent = calculate_total(my_expenses)
    print(f"\n目前共成功記錄 {len(my_expenses)} 筆消費，總計：{total_spent} 元")
```

---

## 3. 方向二：學員成績管理與統計系統（資料管理統計類）

### 一、為什麼選擇這個方向？（設計目的）

老師或助教在整理全班成績時，常需要把分數轉換成等第（如 A、B、C），還要算出平均、最高分、最低分與及格人數。製作「學員成績管理與統計系統」，能有系統地練習**條件判斷（`if / elif / else`）**、**迴圈統計**與**數值範圍檢查**，讓整份報告看起來非常有條理。

### 二、建議期末報告章節大綱

1. **研究背景與動機**
   - 說明人工計算成績容易算錯且耗時的問題。
   - 說明系統目標：自動完成分數驗證、等第判定與全班統計。
2. **系統功能設計與等第規則**
   - 列出功能項目：輸入學員姓名與分數、自動計算等第、顯示班級統計摘要。
   - 用表格定義等第標準（例如：90 以上為 A、80～89 為 B、70～79 為 C、60～69 為 D、未滿 60 為 F）。
3. **核心程式架構與資料結構**
   - 說明如何使用常數 `MAX_SCORE` 與 `MIN_SCORE` 控制分數邊界（0～100 分）。
   - 說明各函式職責：`validate_score`（分數驗證）、`get_grade_level`（等第轉換）、`analyze_scores`（統計計算）。
4. **測試案例與異常處理**
   - 展示輸入 105 分、-5 分或非數字時的防呆提醒。
   - 展示空清單時（沒有任何學員資料）如何避免除以零錯誤（`ZeroDivisionError`，除以零異常）。
5. **成果展示與學習心得**
   - 附上成績報表輸出截圖與計算結果驗證。
   - 整理撰寫過程對程式碼模組化（將大問題拆成小函式）的心得。

### 三、核心範例程式碼（可直接執行）

以下範例示範如何驗證分數是否在 `0～100` 之間、判定等第並產出班級統計摘要：

```python
MIN_SCORE = 0    # 最低合法分數常數
MAX_SCORE = 100  # 最高合法分數常數
PASS_SCORE = 60  # 及格標準常數


def get_grade_level(score):
    """
    依據分數回傳對應的成績等第

    參數：
        score (int | float): 已驗證過的分數（0～100）

    回傳：
        str: 等第代號（A、B、C、D 或 F）
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= PASS_SCORE:
        return "D"
    else:
        return "F"


def register_student_score(score_board, student_name, raw_score):
    """
    檢查分數是否合法後，將學員成績登錄到成績字典中

    參數：
        score_board (dict): 以學員姓名為鍵、分數為值的字典
        student_name (str): 學員姓名
        raw_score (str | int | float): 原始輸入分數

    回傳：
        bool: 登錄成功回傳 True，失敗回傳 False
    """
    try:
        score = float(raw_score)  # 允許輸入整數或小數分數
        if score < MIN_SCORE or score > MAX_SCORE:
            print(f"登錄失敗：{student_name} 的分數 {score} 超出 {MIN_SCORE}～{MAX_SCORE} 範圍。")
            return False
    except ValueError:
        print(f"登錄失敗：{student_name} 的分數「{raw_score}」不是有效數字。")
        return False

    score_board[student_name] = score
    grade = get_grade_level(score)
    print(f"登錄成功：{student_name} 取得 {score} 分（等第 {grade}）")
    return True


def analyze_scores(score_board):
    """
    統計全班成績的平均分、最高分、最低分與及格人數

    參數：
        score_board (dict): 學員成績字典

    回傳：
        dict | None: 統計結果字典；若無資料則回傳 None
    """
    if not score_board:  # 避免清單為空時發生除以零的錯誤
        print("目前沒有任何學員成績資料可供統計。")
        return None

    scores = list(score_board.values())
    passed_count = sum(1 for score in scores if score >= PASS_SCORE)

    return {
        "人數": len(scores),
        "平均分數": round(sum(scores) / len(scores), 2),
        "最高分": max(scores),
        "最低分": min(scores),
        "及格人數": passed_count,
    }


if __name__ == "__main__":
    class_scores = {}

    register_student_score(class_scores, "王小明", 92)
    register_student_score(class_scores, "陳小華", 78.5)
    register_student_score(class_scores, "林大偉", 54)
    register_student_score(class_scores, "張美美", 120)     # 測試超過 100 分
    register_student_score(class_scores, "李小龍", "缺考")  # 測試非數字輸入

    summary = analyze_scores(class_scores)
    if summary:
        print("\n=== 班級成績統計摘要 ===")
        for key, value in summary.items():
            print(f"{key}：{value}")
```

---

## 4. 方向三：終極密碼闖關小遊戲（互動娛樂邏輯類）

### 一、為什麼選擇這個方向？（設計目的）

「終極密碼」是大家最熟悉的互動遊戲：系統先在範圍內隨機藏好一個數字，玩家每次猜測後，系統會縮小提示區間直到猜中為止。選擇小遊戲當作期末專題，不僅能練習**亂數模組（`random`，用來產生隨機數字的內建工具）**與**迴圈狀態更新**，上台報告 Demo 時也能邀請同學現場猜數字，互動感極佳！

### 二、建議期末報告章節大綱

1. **研究背景與動機**
   - 說明選擇文字互動遊戲的原因：規則明確、容易測試邊界條件、適合初學者展現邏輯能力。
2. **遊戲規則與流程設計**
   - 規則說明：預設範圍 `1～100`，最多可猜 7 次（或設定不同難度等級）。
   - 流程步驟：隨機出題 ➔ 玩家輸入猜測數字 ➔ 檢查是否在目前提示區間 ➔ 縮小上下限或判定過關 ➔ 詢問是否重玩。
3. **核心程式架構與設計邏輯**
   - 說明如何使用 `random.randint()` 產生秘密數字。
   - 說明如何用兩個變數（`low_bound` 下限與 `high_bound` 上限）動態縮小提示範圍。
   - 說明如何拆出判斷函式 `check_guess`，讓遊戲主迴圈更好讀。
4. **防呆與邊界測試**
   - 測試輸入文字（如 `"hello"`）時的 `try / except` 防呆。
   - 測試輸入超出目前區間數字（例如範圍已縮到 `35～60`，玩家卻猜 `90`）時如何提醒且不浪費次數。
5. **成果展示與學習心得**
   - 附上完整一局遊玩過程的終端機截圖。
   - 總結自己在迴圈控制與狀態變數更新上的收穫。

### 三、核心範例程式碼（可直接執行）

以下範例示範如何設定亂數答案、檢查玩家猜測並動態更新提示區間（為方便直接執行觀察效果，主程式使用預設測試步驟示範一局遊戲流程；實際專題中可改成 `input()` 與玩家即時互動）：

```python
import random  # 匯入 Python 內建亂數模組

MIN_BOUND = 1    # 遊戲初始最小數字常數
MAX_BOUND = 100  # 遊戲初始最大數字常數


def check_guess(secret_number, guess_number, low_bound, high_bound):
    """
    比對玩家猜測的數字與秘密答案，並回傳結果狀態與更新後的區間

    參數：
        secret_number (int): 系統產生的終極密碼
        guess_number (int): 玩家猜測的數字
        low_bound (int): 目前提示範圍下限
        high_bound (int): 目前提示範圍上限

    回傳：
        tuple[str, int, int]: (狀態字串, 新的下限, 新的上限)
        狀態字串為 "hit"（猜中）、"out_of_range"（超出區間）或 "continue"（繼續猜）
    """
    if guess_number < low_bound or guess_number > high_bound:
        return "out_of_range", low_bound, high_bound

    if guess_number == secret_number:
        return "hit", low_bound, high_bound
    elif guess_number < secret_number:
        return "continue", guess_number + 1, high_bound
    else:
        return "continue", low_bound, guess_number - 1


def parse_player_input(raw_text):
    """
    將玩家輸入的文字安全轉換為整數

    參數：
        raw_text (str): 玩家輸入內容

    回傳：
        int | None: 轉換成功回傳整數，失敗則回傳 None
    """
    try:
        return int(raw_text)
    except ValueError:
        return None


if __name__ == "__main__":
    random.seed(42)  # 固定亂數種子方便展示；正式遊玩時可移除此行讓每局都不同
    secret = random.randint(MIN_BOUND, MAX_BOUND)
    current_low = MIN_BOUND
    current_high = MAX_BOUND
    attempts = 0

    print(f"終極密碼遊戲開始！請猜一個 {current_low}～{current_high} 之間的整數：")

    # 模擬玩家依序輸入（含錯誤輸入與超出範圍測試）
    sample_inputs = ["abc", "150", "50", "75", "85", str(secret)]

    for raw in sample_inputs:
        print(f"\n玩家輸入：{raw}（目前區間：{current_low}～{current_high}）")
        guess = parse_player_input(raw)

        if guess is None:
            print("提示：請輸入有效的整數，這次不扣次數喔！")
            continue

        status, current_low, current_high = check_guess(
            secret, guess, current_low, current_high
        )

        if status == "out_of_range":
            print(f"提示：{guess} 不在目前區間 {current_low}～{current_high} 內，請重猜！")
            continue

        attempts += 1
        if status == "hit":
            print(f"恭喜猜中！終極密碼就是 {secret}，總共有效猜測 {attempts} 次。")
            break
        else:
            print(f"沒猜中！提示範圍縮小為：{current_low}～{current_high}")
```

---

## 5. 個人期末專題執行 5 步驟建議

選定上述任一方向後，建議依照以下 5 個步驟穩紮穩打完成專題與報告：

1. **步驟 1：先做出「最小可行版本」**
   - 不要一開始就想做太多花俏功能，先把最核心的 2～3 個功能寫到能順利跑起來。
2. **步驟 2：拆分成清楚的函式**
   - 將「輸入檢查」、「核心計算／邏輯判斷」、「結果顯示」寫成獨立函式，並採用 `snake_case`（小寫加底線命名法）讓程式碼一目了然。
3. **步驟 3：補上 `try / except` 防呆保護**
   - 思考「如果使用者亂打字、輸入負數、或資料是空的怎麼辦？」，把這些保護都加上去，這在期末評分非常加分。
4. **步驟 4：準備 3～5 組測試案例並截圖**
   - 分別測試「正常操作」與「故意輸入錯誤資料」的執行結果，並在 VS Code（Visual Studio Code 編輯器）中將終端機輸出截圖，直接貼進報告當作成果證明。
5. **步驟 5：完成書面報告與口頭簡報重點**
   - 按照「背景動機 ➔ 功能與流程 ➔ 程式說明 ➔ 測試與心得」的順序整理文件，口頭報告時現場操作一次程式給大家看最有說服力！

---

## 6. 重點整理

- **選題原則**：選一個自己最有興趣、且能在期限內「完整寫完並測試通過」的主題，**完整度比貪多更重要**。
- **三個方向一句話選擇法**：
  - 想做實用小工具 ➔ 選 **方向一：個人日常記帳小幫手**
  - 想展現嚴謹統計與資料管理 ➔ 選 **方向二：學員成績管理與統計系統**
  - 想讓 Demo 互動有趣、邏輯鮮明 ➔ 選 **方向三：終極密碼闖關小遊戲**
- **程式碼品質加分關鍵**：
  - 統一使用 **4 個空格縮排**、**`snake_case` 命名**、**大寫常數**，並為每個函式寫上清楚的**繁體中文說明文件（docstring）與行內註解**。
