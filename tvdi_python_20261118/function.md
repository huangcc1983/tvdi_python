# Python 函式呼叫學習講義

> **課程代碼**：TVDI Python 20261118  
> **使用工具**：Herd（Herdr）、Visual Studio Code  
> **學習目標**：能夠理解並實作 Python 函式的定義與呼叫

---

## 📋 目錄

1. [環境準備](#1-環境準備)
2. [認識函式（Function）](#2-認識函式function)
3. [定義與呼叫函式](#3-定義與呼叫函式)
4. [函式參數](#4-函式參數)
5. [函式回傳值](#5-函式回傳值)
6. [實戰練習](#6-實戰練習)
7. [常見錯誤與排除](#7-常見錯誤與排除)

---

## 1. 環境準備

### 1.1 安裝 Herd（Herdr）

Herd 是一套輕量化的本地開發環境管理工具，可以讓你快速切換 Python 版本、管理虛擬環境。

**步驟：**

1. 前往 Herd 官網或 GitHub 下載安裝程式
2. 依照安裝精靈完成安裝
3. 開啟 Herd，新增一個 **Python 專案環境**
4. 確認 Python 版本（建議 Python 3.10+）

```bash
# 在 Herd 終端機中確認 Python 版本
python --version
```

---

### 1.2 安裝 Visual Studio Code

1. 前往 [https://code.visualstudio.com](https://code.visualstudio.com) 下載並安裝 VS Code
2. 開啟 VS Code，安裝以下擴充功能（Extensions）：
   - **Python**（Microsoft 官方）
   - **Pylance**（智慧型程式碼提示）
   - **Python Indent**（縮排輔助）

> **提示**：按下 `Ctrl + Shift + X` 開啟擴充功能市集搜尋安裝

---

### 1.3 在 VS Code 中連結 Herd 環境

1. 在 VS Code 中按下 `Ctrl + Shift + P`
2. 搜尋並選擇 **「Python: Select Interpreter」**
3. 選擇 Herd 所建立的 Python 虛擬環境路徑
4. 右下角狀態列應顯示對應的 Python 版本

---

## 2. 認識函式（Function）

### 什麼是函式？

函式是一段**有名字、可重複使用的程式碼區塊**。  
當你發現某段程式碼需要重複執行，就應該把它包裝成函式。

```
輸入（參數）→ [函式] → 輸出（回傳值）
```

### 為什麼要用函式？

| 優點 | 說明 |
|------|------|
| ♻️ 重複使用 | 寫一次，呼叫多次 |
| 📦 模組化 | 程式碼結構更清晰 |
| 🐛 易於除錯 | 問題範圍縮小到函式內 |
| 👥 團隊協作 | 各人負責不同函式 |

---

## 3. 定義與呼叫函式

### 3.1 語法結構

```python
def 函式名稱():
    # 函式內容（需縮排 4 個空格）
    程式碼
```

### 3.2 步驟示範

**步驟 1：** 在 VS Code 中新增檔案 `function_practice.py`

**步驟 2：** 定義一個最簡單的函式

```python
def say_hello():
    print("Hello, Python!")
```

**步驟 3：** 呼叫函式

```python
say_hello()   # 呼叫函式
say_hello()   # 可以多次呼叫
```

**步驟 4：** 執行程式

在 VS Code 終端機（`Ctrl + ~`）輸入：

```bash
python function_practice.py
```

**預期輸出：**
```
Hello, Python!
Hello, Python!
```

> **重點**：定義函式不會執行它，**必須呼叫才會執行**！

---

## 4. 函式參數

### 4.1 傳入參數

讓函式接受外部資料：

```python
def greet(name):
    print(f"哈囉，{name}！")

# 呼叫時傳入值
greet("小明")
greet("小華")
```

**輸出：**
```
哈囉，小明！
哈囉，小華！
```

---

### 4.2 多個參數

```python
def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add(3, 5)
add(10, 20)
```

---

### 4.3 預設參數值

```python
def greet(name, language="繁體中文"):
    print(f"以 {language} 打招呼：哈囉，{name}！")

greet("小明")               # 使用預設值
greet("John", "English")   # 覆蓋預設值
```

---

### 4.4 關鍵字參數（Keyword Arguments）

```python
def profile(name, age, city):
    print(f"姓名：{name}，年齡：{age}，城市：{city}")

# 用關鍵字傳入，順序可不同
profile(age=25, city="台北", name="小明")
```

---

## 5. 函式回傳值

### 5.1 使用 `return`

```python
def multiply(a, b):
    return a * b

# 接收回傳值
answer = multiply(4, 5)
print(answer)   # 輸出：20
```

### 5.2 回傳多個值

```python
def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference

t, d = calculate(10, 3)
print(f"總和：{t}，差值：{d}")
```

### 5.3 有無 `return` 的差異

```python
def with_return(x):
    return x * 2       # 有回傳值

def without_return(x):
    print(x * 2)       # 只印出，無回傳值

result1 = with_return(5)
result2 = without_return(5)

print(result1)   # 10
print(result2)   # None（無回傳值時預設為 None）
```

---

## 6. 實戰練習

### 🏋️ 練習一：BMI 計算器

**目標**：寫一個函式計算 BMI 並判斷體重狀態

```python
def calculate_bmi(weight, height):
    """
    計算 BMI 值
    weight: 體重（公斤）
    height: 身高（公尺）
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def judge_bmi(bmi):
    if bmi < 18.5:
        return "體重過輕"
    elif bmi < 24:
        return "體重正常"
    elif bmi < 27:
        return "體重過重"
    else:
        return "肥胖"

# 主程式
my_bmi = calculate_bmi(70, 1.75)
status = judge_bmi(my_bmi)

print(f"BMI：{my_bmi}，狀態：{status}")
```

---

### 🏋️ 練習二：簡易成績計算

**目標**：計算多科成績的平均，並回傳等第

```python
def average(scores):
    return sum(scores) / len(scores)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# 測試
scores = [85, 92, 78, 90, 88]
avg = average(scores)
g = grade(avg)

print(f"平均分數：{avg:.1f}，等第：{g}")
```

---

## 7. 常見錯誤與排除

| 錯誤類型 | 錯誤原因 | 解決方式 |
|----------|----------|----------|
| `IndentationError` | 縮排不正確（混用空格與 Tab） | 統一使用 4 個空格 |
| `NameError` | 呼叫未定義的函式 | 確認函式定義在呼叫之前 |
| `TypeError` | 參數數量不符 | 確認傳入參數與定義一致 |
| 函式無輸出 | 忘記加 `return` 或 `print()` | 確認函式內有輸出指令 |
| `SyntaxError` | 忘記冒號 `:` | 在 `def` 行末加上 `:` |

---

## 📌 學習重點總結

```
1. def 函式名稱():     → 定義函式
2. 函式名稱()          → 呼叫函式
3. def f(參數):        → 傳入資料
4. return 值           → 回傳結果
5. 縮排必須一致（4 空格）
```

---

## 🔗 延伸學習資源

- [Python 官方文件 - 函式](https://docs.python.org/zh-tw/3/tutorial/controlflow.html#defining-functions)
- [VS Code Python 教學](https://code.visualstudio.com/docs/python/python-tutorial)

---

> 📝 **講義版本**：v1.0 ｜ **日期**：2026-11-18  
> 如有問題請於課堂中提問或至課程討論區發問。
