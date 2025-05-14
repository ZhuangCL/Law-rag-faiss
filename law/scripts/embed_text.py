import openai
import numpy as np

def embed_text(text):
    response = openai.embeddings.create(
        model="text-embedding-ada-002",  # 或你現在用的 embedding 模型
        input=text
    )
    embedding = response.data[0].embedding
    return np.array(embedding, dtype='float32')

