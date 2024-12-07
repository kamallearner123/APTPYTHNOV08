import asyncio

global_counter = 0

lock = asyncio.Lock()

async def modify_shared_counter(sem, myid):
    global global_counter
    async with sem:
        print("Going to increment counter by ", myid)
        await asyncio.sleep(1)
        global_counter += 1
        print("Going to increment counter by ", myid)

async def main():
    sem = asyncio.Semaphore(5)
    await asyncio.gather(*(modify_shared_counter(sem, i) for i in range(10)))


asyncio.run(main())





