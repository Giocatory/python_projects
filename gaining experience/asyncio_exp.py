import asyncio

async def ticker(delay, to):
    for i in range(to):
        yield (i, delay)
        await asyncio.sleep(delay)
        
async def run(k):
    async for i in ticker(k, 5):
        print(i)

async def main():
    task1 = asyncio.create_task(run(0.5))
    task2 = asyncio.create_task(run(1))
    # планируем одновременные вызовы:
    await asyncio.gather(task1, task2)


if __name__ == '__main__':
    asyncio.run(main())
    
# (0, 0.5)
# (0, 1)
# (1, 0.5)
# (1, 1)
# (2, 0.5)
# (3, 0.5)
# (2, 1)
# (4, 0.5)
# (3, 1)
# (4, 1)