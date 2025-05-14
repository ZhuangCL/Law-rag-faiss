from scripts.rag_qa import search_law, extract_keywords, print_law

def main():
    # Step 1: 資料爬取
    # 到scripts資料夾裡執行crawl_law_articles()

    # Step 2: 建立 FAISS 索引
    # 到scripts資料夾裡執行create_faiss_index()

    # Step 3: 問題輸入與查詢
    query = input("請輸入你想搜尋的法條問題：")
    keywords = extract_keywords(query)
    print(f"🔍 擷取關鍵字：{keywords}")
    law_indexes = search_law(query)
    
    # Step 4: 顯示結果
    print_law(law_indexes, keywords)

if __name__ == "__main__":
    main()