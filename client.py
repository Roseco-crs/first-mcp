from fastmcp import Client
import asyncio

# Point the client to the server file. Or connects the client directly to the server instance
client = Client("server.py") 

# Testing in trust MCP server
async def test_greet(name: str):
    async with client:
        is_alive = await client.ping()     # Ping the server
        tools = await client.list_tools()   # List available the tools
        response = await client.call_tool("greet", {"name": name})     # Call a specific tool
        # content = await client.read_resource("resource://your/data")   # Read a resource  
        print("Ping: ", is_alive)
        print("tools: ", tools)
        print("response: ", response)


asyncio.run(test_greet("Beatrice Nannh"))


# Note: There are two things to know
# 1) Clients are asynchronous, so we need to use asyncio.run to run the clients
# 2) We must enter a client context (async with client: ) before using the client.
#    We can make multiple client calls within the same context.