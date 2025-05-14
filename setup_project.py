import os

# 定義專案資料夾結構
project_structure = {
    "law": [  # 根目錄資料夾
        "embeddings",     # 存儲 FAISS 向量資料庫的資料夾
        "scripts",         # 存儲所有腳本的資料夾
    ]
}

# 定義需要創建的檔案清單
files = [
    "law/main.py",              # 主程式：執行入口
    "law/requirements.txt",     # 依賴套件清單
    "law/config.py",            # API 金鑰與設定
    "law/README.md",            # 專案說明文件
    "law/data/traffic_raw.json", # 存儲爬蟲結果的原始資料檔案
    "law/scripts/crawler.py",   # 爬蟲程式：爬取法條資料
    "law/scripts/embed_faiss.py", # FAISS 向量化程式
    "law/scripts/rag_qa.py",    # 問答邏輯程式：檢索與回答
]

# 建立資料夾結構
for folder, subfolders in project_structure.items():
    os.makedirs(folder, exist_ok=True)  # 創建根資料夾
    for subfolder in subfolders:
        os.makedirs(os.path.join(folder, subfolder), exist_ok=True)  # 創建子資料夾

# 建立檔案
for file in files:
    file_path = os.path.join(file)  # 定位檔案位置
    with open(file_path, "w") as f:
        pass  # 創建空檔案

# 顯示完成訊息
print("✅ 專案檔案結構已建立完成！")