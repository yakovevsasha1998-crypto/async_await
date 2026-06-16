import asyncio
import time

async def say_hello():
    await asyncio.sleep(2)
    print('hello!')

async def say_hello1():
    await asyncio.sleep(1)
    print('hello1')

async def main():
    start = time.time()
    await asyncio.gather(say_hello(),say_hello1())
    print(f'Заняло: {time.time() - start:.1f} сек')

asyncio.run(main())