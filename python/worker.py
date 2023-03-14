import asyncio
import handler

class Worker:

    def __init__(self, queue: asyncio.Queue, workers_number: int):
        self.queue = queue
        self.workers = workers_number

    async def handler(self, data):
        await handler.handler(data)

    async def worker(self):
        while True:
            data = await self.queue.get()
            await self.handler(data)

    async def start(self):
        for _ in range(self.workers):
            asyncio.create_task(self.worker())
