import os
import json
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

async def run_scan():
    try:
        api_id = int(os.getenv('TG_API_ID'))
        api_hash = os.getenv('TG_API_HASH')
        session_str = os.getenv('TG_SESSION')

        channels = ['MoviesIsrael', 'Sratim_IL', 'Netflix_Movies_IL']
        all_movies = []

        async with TelegramClient(StringSession(session_str), api_id, api_hash) as client:
            for channel in channels:
                try:
                    # סורק 150 הודעות אחרונות כדי למצוא סרטים אמיתיים
                    async for message in client.iter_messages(channel, limit=150):
                        # בודק אם יש טקסט, ואם מצורף קובץ או וידאו
                        if message.text and (message.video or message.document):
                            text = message.text
                            # מסנן הודעות שהן בעצם פרסומות לקבוצות אחרות
                            if "הצטרפו" not in text and "קבוצה" not in text and "VIP" not in text:
                                title = text.split('\n')[0][:60] # לוקח רק את שורת הכותרת
                                title = title.replace('*', '').replace('_', '').strip() # מנקה סימנים מיותרים
                                
                                link = f"https://t.me/{channel}/{message.id}"
                                all_movies.append({"name": title, "link": link})
                except Exception:
                    pass
        
        with open('movies_data.json', 'w', encoding='utf-8') as f:
            json.dump(all_movies, f, ensure_ascii=False, indent=4)

    except Exception as e:
        exit(1)

if __name__ == "__main__":
    asyncio.run(run_scan())
