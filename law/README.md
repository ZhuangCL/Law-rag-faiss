# LawQ&A - 法律條文智能問答系統

本專案整合 FAISS 向量資料庫與 OpenAI GPT 模型，實現法律條文的語意搜尋與問答功能。使用者可以輸入自然語言問題，系統會自動提取關鍵字，並從法條資料中找出最相關內容。

## 📁 專案結構

law/ ├── main.py # 主入口，整合整體流程 
├── scripts/ │ ├── crawler.py # 法條爬蟲（可選） │ 
├── embed_text.py # embedding 處理邏輯 │ 
├── embed_faiss.py # 將法條嵌入並儲存至 FAISS │
├── rag_qa.py # 問答邏輯與關鍵字擷取 ├── embeddings/ │
  ├── traffic_texts.json # 法條文本 JSON 格式 │ 
  └── traffic_faiss.index # FAISS 索引檔

## 🚀 使用方式

1. 安裝必要套件：
    ```bash
    pip install -r requirements.txt
    ```

2. 執行主程式：
    ```bash
    python main.py
    ```

3. 根據提示輸入問題，例如：
    ```
    請輸入你想搜尋的法條問題：酒後駕駛的罰鍰
    ```

## 📌 功能介紹

- 🔍 自動提取使用者問題的法律關鍵字
- 📚 使用 FAISS 向量檢索最相關法條
- 🤖 利用 LLM 模型進行語意擷取與問答

## 📦 環境需求

- Python 3.8+
- OpenAI API Key

## 📄 資料來源

- 法條爬蟲可自定義爬取各法律網站（如《法律命令資料庫》）
