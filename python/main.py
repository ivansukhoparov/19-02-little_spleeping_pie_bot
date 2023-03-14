import asyncio
from poller import Poller
from worker import Worker


async def start():
    queue = asyncio.Queue()
    poller = Poller(queue)
    await poller.start()
    worker = Worker(queue, 5)
    await worker.start()

def run():
    loop=asyncio.get_event_loop()
    try:
        print('bot started')
        loop.create_task(start())
        loop.run_forever()
    except KeyboardInterrupt:
        pass

def min_to_hours(time_in_min):
  mins = int(time_in_min) % 60
  hours = (int(time_in_min) - mins) / 60
  if mins<10:
    mins = '0' + str(mins)
  str_time = str(int(hours)) + ':' + str(mins)
  return str_time

def init():
    shedule = {}
    for i in range(1440):
        time = min_to_hours(i)
        shedule[time] =[]    

init()
run()   



