import asyncio
import tg_client

class Poller:
   
    def __init__ (self, queue: asyncio.Queue):
        self.queue = queue

    async def collector(self): 
        client = tg_client.TelegramClient
        offset = 0
        while True:
            response = await client.get_updates(offset=offset)

            for item in response['result']:
                offset = item["update_id"] + 1
                self.queue.put_nowait(item)

    async def start(self):
        asyncio.create_task(self.collector())

