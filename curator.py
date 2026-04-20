import json
import random
import datetime

# 模擬音樂資料庫
music_pool = [
    {"title": "Plastic Love", "artist": "竹內瑪莉亞", "reason": "經典 City Pop，符合你的復古審美。"},
    {"title": "Subtitle", "artist": "Official髭男dism", "reason": "現代流行神曲，編曲精緻度高。"},
    {"title": "花火", "artist": "aiko", "reason": "情緒渲染力強，適合散步聽。"},
    {"title": "閃光", "artist": "Alexandros", "reason": "節奏感強烈，平衡網站的悠閒感。"},
    {"title": "Tokyo Flash", "artist": "Vaundy", "reason": "當紅新聲，具有強烈的都市氣息。"}
]

def generate_recommendations():
    # 隨機挑選 5 首歌曲模擬 AI 分析
    recommendations = random.sample(music_pool, 3) # 這裡改為選3-5首
    
    # 寫入 json 檔案
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(recommendations, f, ensure_ascii=False, indent=4)
    
    print(f"[{datetime.datetime.now()}] 成功更新 5 首推薦歌曲！")

if __name__ == "__main__":
    generate_recommendations()