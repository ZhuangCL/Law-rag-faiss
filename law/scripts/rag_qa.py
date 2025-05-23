# _________________________________________________OPENAI LLM
import faiss
import json
import openai
from scripts.embed_text import embed_text  # 你自己定義好的 embedding 函數
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# 設定 OpenAI API 金鑰
import config
openai.api_key = config.OPENAI_API_KEY

# 建立 LangChain LLM (對應 gpt-3.5-turbo)
llm = ChatOpenAI(model_name="gpt-3.5-turbo", api_key = config.OPENAI_API_KEY,temperature=0)

# 載入 FAISS 索引
index = faiss.read_index("embeddings/traffic_faiss.index")
with open('scripts/law/data/traffic_raw.json', 'r', encoding='utf-8') as f:
    laws_data = json.load(f)

# 定義 Prompt 模板
keyword_prompt = PromptTemplate(
    input_variables=["query"],
    template=(
        "請根據下列問題，提取字數不超過1的關鍵字，用逗號分隔。\n"
        "問題：{query}"
    )
)
keyword_chain = LLMChain(prompt=keyword_prompt, llm=llm)
# 切割關鍵字
def extract_keywords(query):
    response = keyword_chain.run(query)
    keywords = [kw.strip() for kw in response.split(",") if kw.strip()]
    return keywords


# FAISS 搜尋法條
def search_law(query, k=20):
    # 將查詢轉換為嵌入向量
    query_vector = embed_text(query)

    # 在 FAISS 中檢索最相似的法條
    D, I = index.search(query_vector.reshape(1, -1), k)

    # 返回檢索到的法條
    return I

from tqdm import tqdm
def print_law(law_indexes, keywords):
    for i in tqdm(law_indexes[0]):
        law = laws_data[i]
        law_text = f"{law['title']} {law['content']}"
        
        if all(keyword in law_text for keyword in keywords):
            print(f"✅ 找到相關法條📄：{law_text}")
