import asyncio


async def hi():
    print("Hi")
    await asyncio.sleep(3)
    print("Pkmer")

asyncio.run(hi(), debug=True)
