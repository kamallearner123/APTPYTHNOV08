import asyncio

async def set_future(future, sec):
    await asyncio.sleep(sec)
    future.set_result(100)
    print("Setting future is done!!!")


async def main():
    # Creat event loop
    loop = asyncio.get_running_loop()
    # Creat a future event
    future = loop.create_future()

    print("Created async task along with future")
    asyncio.create_task(set_future(future, 10))

    print("Awaiting for the future to be set")
    result = await future
    print("Result = {}", result)


asyncio.run(main())

