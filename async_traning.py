import asyncio


async def useful_foo():
    print('Start')
    await asyncio.sleep(2)
    print('Finish')


async def async_tasker():
    tasks = []
    for i in range(5):
        tasks.append(asyncio.create_task(useful_foo()))
    await asyncio.gather(*tasks)


def main():
    asyncio.run(async_tasker())


if __name__ == '__main__':
    main()
