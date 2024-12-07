import asyncio

async def wait_fun(event):
    await asyncio.sleep(1)
    print("Waiting for the event")
    await event.wait()
    print("Waited for event await")

async def set_fun(event):
    await asyncio.sleep(2)
    event.set()
    

async def main():
    event = asyncio.Event()

    await asyncio.gather(set_fun(event), wait_fun(event))
    

asyncio.run(main())
