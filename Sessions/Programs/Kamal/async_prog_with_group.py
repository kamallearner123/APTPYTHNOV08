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
    return sec

async def main():
    print("1. Main function is started!!!")
    print("2. Going to call fetch data function!!!")
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([10, 20, 30]):
            task = tg.create_task(fetchdata(sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks] 

    print("7. Main: fetchdata task is done :)")
    print("Results = ", results)


asyncio.run(main())


