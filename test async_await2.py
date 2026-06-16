import asyncio
import random

async def handle_users(user_id:int):
    print(f'Пользователь {user_id} подключился')
    await asyncio.sleep(random.randint(1,3))
    print(f'Пользователь {user_id} получил ответ')

async def main():
    await asyncio.gather(
        handle_users(1),
        handle_users(2),
        handle_users(3)
    )

asyncio.run(main())




