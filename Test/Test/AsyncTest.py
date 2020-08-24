# -*- coding: utf-8 -*-
# author: Avimitin
# datetime: 2020/8/24 10:11
import asyncio
import time


async def say_after(delay: int, words: str):
    # 可以看到两个任务是同时运行的
    print("TASK START AT %s" % time.strftime('%x'))
    await asyncio.sleep(delay)
    print(words)
    print("TASK OVER, USE %d SEC" % delay)


async def main():
    ASYNC_TASK = []
    task1 = asyncio.create_task(say_after(1, "async"))
    task2 = asyncio.create_task(say_after(2, "test"))
    ASYNC_TASK.append(task1)
    ASYNC_TASK.append(task2)

    while ASYNC_TASK:
        await ASYNC_TASK.pop()

if __name__ == '__main__':
    asyncio.run(main())
