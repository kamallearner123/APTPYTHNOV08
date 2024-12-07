import asyncio

global_counter = 0

lock = asyncio.Lock()

async def modify_shared_counter(myid):
    global global_counter
    async with lock:
        print("Going to increment counter by ", myid)
        await asyncio.sleep(1)
        global_counter += 1
        print("Going to increment counter by ", myid)

async def main():
    await asyncio.gather(*(modify_shared_counter(i) for i in range(10)))


asyncio.run(main())





