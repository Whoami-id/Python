import random
import time
import asyncio

async def foo():
    print("42")
    await asyncio.sleep(1)
    print("1337")


async def main():
    await asyncio.gather(foo(), foo(),foo(), foo())




async def produce(id: int, q: asyncio.Queue):
    sleep_time =  random.randint(0, 5)
    await asyncio.sleep(sleep_time)
    await  q.put(random.randint(0, 42))
    print("Producer: " + str(id) + " ist fertig")


async def consume(id: int, q: asyncio.Queue):
    while True:
        sleep_time = random.randint(0, 5)
        await asyncio.sleep(sleep_time)
        var = await q.get()
        print("Consumer: " + str(id) + " hat das Element " + str(var) + " erhalten")
        q.task_done()

async def main2(n = 42):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(id, q)) for id in range(n)]
    consumers = [asyncio.create_task(consume(id, q)) for id in range(n)]
    await asyncio.gather(*producers)
    await q.join()
    for c in consumers:
        c.cancel()

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main2())
    end = time.time()
    print(str(end - start))

