from fastmcp import Client
import asyncio

### --- A 2nd client ---- ####

async def test_division(a: int, b: int):
    async with Client("mathserver.py") as mathclient:
        result = await mathclient.call_tool("division", {"a": a, "b": b})
        print(f"The result of {a} divided by {b} is: {result}")

async def test_modulo(a: int|float, b: int|float):
    async with Client("mathserver.py") as mathclient:
        result = await mathclient.call_tool("modulo", {"a": a, "b": b})
        print(f"The result of {a} modulo {b} is: {result}")

asyncio.run(test_modulo(100, 17.5))
asyncio.run(test_division(15.18, 17))