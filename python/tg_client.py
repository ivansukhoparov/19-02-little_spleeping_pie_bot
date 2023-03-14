from typing import Optional
import aiohttp
import bot_token


class TelegramClient:

  async def get_updates(offset: Optional[int] = None, timeout: int = 0) -> dict:
      url = f"https://api.telegram.org/bot{bot_token.TOKEN}/getUpdates"
      params = {}
      if offset:
        params['offset'] = offset
      if timeout:
        params['timeout'] = timeout
      async with aiohttp.ClientSession() as session:
          async with session.get(url, params = params) as response:
              return await response.json()
          
  async def send_message(chat_id: int, text: str):
      url = f"https://api.telegram.org/bot{bot_token.TOKEN}/sendMessage"
      payload = {
        'chat_id': chat_id,
        'text': text
      }
      async with aiohttp.ClientSession() as session:
        async with session.post(url, json = payload) as response:
          return await response.json()  