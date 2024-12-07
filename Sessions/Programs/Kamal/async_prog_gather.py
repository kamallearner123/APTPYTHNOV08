'''
# Async Programming in Python :)

- Reference: [https://www.youtube.com/watch?v=Qb9s3UiMSTA]

## Prparedness:
-  "asyncio" as part of Python 3.11 onwards

## Coroutine:
- What?
      When a function is define with "async" attached, it is called as coroutine function.
- asyncio.run: Makes sure that async function runs and joins
- If we call main(): It returns an object, but does not execute. Then we should call "await obj" to wait until the job is done.

## await task



'''
import time
import asyncio

async def fetchdata(sec):
    print("3. Fun: fetchdata: Started")
    print("4. Fun: fetchdata: waiting to collect the data: for ",sec)
    await asyncio.sleep(sec)
    print("6. Fun: fetchdata: done with collecting the data: for ", sec)


async def main():
    print("1. Main function is started!!!")
    print("2. Going to call fetch data function!!!")
    print("5. Waiting to finish task!!!")
    await asyncio.gather(fetchdata(10), fetchdata(20), fetchdata(30))
    print("7. Main: fetchdata task is done :)")


asyncio.run(main())


