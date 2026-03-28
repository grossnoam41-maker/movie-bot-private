import os
import json
import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

async def run_scan():
    try:
        # הקודים האישיים שלך:
        api_id = 39822690
        api_hash = '18c86b21592ffc11acd1ea1af8ad11ad'
        session_str = '1BJWap1wBu61ilN1n1V7g-sYzCaKYsQXHvlaci3MNyrM1FpVx5jGlHCimAby5HlqFWw5mJ4-c4KwIIEMzvjqbKvTtrTiU-1cJJcWGYp7nHwy5LoJ5o2DEvQHXRjBl6D7dnClot_A0jWt8-HTMGbeEaa5_rkQMZ8otg4xjkJqWdkdsdxliBR8ru03K_uviGDcqnMH3DPiPRQSlIXuquSJPtt7fBrWHri96xt6XAORZSNJo26j46tEiEX-SmF5zo3kQVaXHuhLpAJnWbo50W9AYB8AJTVbwzEABxJNus7LZHgEB4-rpnsvIiSnqnOZqFl6fEkGBTFt-aMqYCkwk7VjFYd29VdG4XSM='

        channels = ['MoviesIsrael', 'Sratim_IL', 'Netflix_Movies_IL']
        all_movies = []

        async with TelegramClient(StringSession(session_str), api_id, api_hash) as client:
            for channel in channels:
                print(f"סורק את: {channel}...")
                try:
                    async for message in client.iter_messages(channel, limit=50):
                        if message.video and message.text:
                            title = message.text.split('\n')[0][:60]
                            link = f"https://t.me/{channel}/{message.id}"
                            all_movies.append({"name": title, "link": link})
                except Exception as e:
                    print(f"דילוג על {channel} בגלל שגיאה: {e}")
        
        with open('movies_data.json', 'w', encoding='utf-8') as f:
            json.dump(all_movies, f, ensure_ascii=False, indent=4)
        print(f"הסריקה הושלמה! נמצאו {len(all_movies)} סרטים.")

    except Exception as e:
        print(f"שגיאה: {e}")
        exit(1)

if __name__ == "__main__":
    asyncio.run(run_scan())
