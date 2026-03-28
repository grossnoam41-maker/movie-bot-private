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
                    # סורק 100 הודעות אחרונות
                    async for message in client.iter_messages(channel, limit=100):
                        # התנאי החדש: אם יש טקסט, והוא ארוך מ-10 אותיות - תיקח אותו!
                        if message.text and len(message.text) > 10:
                            # לוקח רק את השורה הראשונה בתור כותרת
                            title = message.text.split('\n')[0][:60].strip()
                            title = title.replace('*', '').replace('_', '')
                            
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
