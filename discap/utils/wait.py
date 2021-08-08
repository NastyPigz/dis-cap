import asyncio, datetime, concurrent

async def wait_until(time:datetime.datetime):
    def _wait(time):
        while True:
            if ((time-datetime.datetime.utcnow()) <= datetime.timedelta(seconds=0)):
                break
        return True
    loop = asyncio.get_running_loop()
    async def blocking():
        with concurrent.futures.ThreadPoolExecutor() as pool:
            await loop.run_in_executor(pool, _wait, time)
    finished = await loop.create_task(blocking())
    return finished