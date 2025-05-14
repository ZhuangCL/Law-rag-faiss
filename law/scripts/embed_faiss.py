import json
import os
import faiss
import numpy as np
from openai import OpenAI
from tqdm import tqdm 

# 載入 config（放 API 金鑰用）
import config

# 設定 OpenAI API 金鑰
openai = OpenAI(api_key=config.OPENAI_API_KEY)

# 載入條文資料
with open("law/data/traffic_raw.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

# 產生 embedding 用的函式
def get_embedding(text):
    response = openai.embeddings.create(
        input=text,
        model="text-embedding-ada-002"
    )
    return np.array(response.data[0].embedding)

# 建立儲存用的資料夾
os.makedirs("../embeddings", exist_ok=True)

# 要放進 FAISS 的 embedding 與對應文本
embedding_list = []
text_list = []

for article in tqdm(articles, desc="處理法條中"):
    combined_text = f"{article['title']} {article['content']}"
    text_list.append(combined_text)
    embedding = get_embedding(combined_text)
    embedding_list.append(embedding)

# 轉成 numpy array
embedding_matrix = np.vstack(embedding_list)

# 建立 FAISS index（使用 L2 距離）
dimension = embedding_matrix.shape[1]
index = faiss.IndexFlatL2(dimension)

# 加入資料
index.add(embedding_matrix)

# 儲存 FAISS index
faiss.write_index(index, "../embeddings/traffic_faiss.index")

# 同步儲存對應的文本，方便之後問答檢索時對應
with open("../embeddings/traffic_texts.json", "w", encoding="utf-8") as f:
    json.dump(text_list, f, ensure_ascii=False, indent=2)

print(f"✅ 已完成 {len(embedding_list)} 筆 embedding 並儲存 FAISS 資料庫！")