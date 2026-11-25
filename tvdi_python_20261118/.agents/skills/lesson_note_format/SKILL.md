---
name: lesson_note_format
description: >-
  Enforces the required top header format whenever creating any new Markdown
  (.md) document in this project. Use this skill every time a new .md file
  (such as lecture notes, guides, outlines, or plans) is created so that
  **建立日期** (creation date) and **重點摘要** (key summary) are included
  at the very top of the file.
---

# 課程筆記與 Markdown 文件開頭格式規範（lesson_note_format）

## 目的

確保本專案中每一份新建的 Markdown（`.md`）講義、筆記或規劃文件在打開的第一時間，都能清楚呈現「建立時間」與「核心內容摘要」，方便學員快速複習與整理進度。

---

## 適用與排除範圍

- **適用範圍**：在本專案內新建任何教學講義、筆記、企劃、報告大綱等 `.md` 檔案時，必須套用本格式規範。
- **排除範圍**：代理系統設定檔與結構化設定檔（例如 `GEMINI.md`、`AGENTS.md`、`SKILL.md`）不適用此格式，避免破壞系統設定或 YAML Frontmatter（檔頭中繼資料）語法。

---

## 標準開頭格式範本

新建 `.md` 檔案時，必須將以下區塊置於**檔案最上方（第 1 行起）**：

```markdown
**建立日期**：YYYY-MM-DD  
**重點摘要**：用 1～3 句繁體中文簡要說明本文件的核心主題、學習目標與主要內容。

---

# 文件主標題
```

> **排版提醒**：`**建立日期**：YYYY-MM-DD` 行尾保留兩個半形空格（或各自獨立分段），以確保在 Markdown 預覽畫面中與 `**重點摘要**` 分行顯示。

---

## 執行步驟

1. **取得並格式化建立日期**：確認當天系統日期，統一以 `YYYY-MM-DD` 格式填寫（例如：`2026-11-25`）。
2. **撰寫初學者友善的重點摘要**：用 1～3 句白話的繁體中文，先說明「這份文件要解決什麼問題／學到什麼」，再簡述核心內容。
3. **套用開頭結構並銜接正文**：將 `**建立日期**` 與 `**重點摘要**` 固定放在檔案最上方，接續分隔線 `---` 與 `# 文件主標題`；後續目錄、程式碼區塊與表格皆須同時遵守專案 `GEMINI.md` 規範。
4. **建立後驗證檢查**：檔案寫入完成後，確認第 1～3 行確實包含 `**建立日期**` 與 `**重點摘要**`、日期格式正確，且全文無簡體中文誤植。
