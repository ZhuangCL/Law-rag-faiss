import requests
from bs4 import BeautifulSoup
import json

# 設定目標網址
url = "https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=K0040012"

# 發送 HTTP 請求
response = requests.get(url)
response.encoding = 'utf-8'

# 使用 BeautifulSoup 解析 HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 找到所有條文的區塊
data = []

# 定位每條條文
law_sections = soup.find_all('div', class_='row')

# 逐一抓取條文標題與內容
for section in law_sections:
    try:
        title_elem = section.find('a')
        content_elem = section.find('div', class_='law-article')

        if title_elem and content_elem:
            title = title_elem.text.strip()
            content = content_elem.get_text(strip=True)
            if title and content:
                data.append({"title": title, "content": content})

    except Exception as e:
        print(f"錯誤: {e}")

# 儲存為 json
with open("law/data/traffic_raw.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"✅ 成功爬取 {len(data)} 條條文，已儲存到 law/data/traffic_raw.json")
