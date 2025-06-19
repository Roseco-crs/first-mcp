## Quickstart MCP project
Welcome to my first quickstart MCP.

## What is MCP?

MCP stands for Model Context Protocol. It is an open source protocol to standardize LLM applications or standardized way to provid context and tools to our LLMs.

## FastMCP
FastMCP makes building MCP servers and clients simple and intuitive. 

## Components
FastMCP servers expose many types of components to the client.
### Tools 
Tools are functions that the client can call to perform actions or access external systems.

### Resources 
Resources expose data sources that the client can read.

### Resource Templates
Resource Templates are parameterized resources that allow the client to request a specific data.

### Prompts
Prompts are reusable message templates for guiding the LLM.


## Key Points
* Clients are asynchronous, so we need to use <asyncio.run()> to run the clients
* We must enter a client context (<async with client: >) before using the client. We can make multiple client calls within the same context.
* To run the server, we can to use <mcp.run> in the <__main__> block. Nevertheless, this not mandatory.
* To have FastMCP run the server for us, we need to use <fastmcp run > command. For example: <fastmcp run server.py:mcp>
* Note that FastMCP does not require the <__main__> block in the server file, and will ignore it if it is present. Instead, it looks for the server object provided in the CLI command (here, <mcp>). If no server object is provided, fastmcp run will automatically search for servers called “mcp”, “app”, or “server” in the file.
* Don't forget to point the server file while creating an instance of the your client. For instance: <from fastmcp import Client
               client = Client("server.py")>


## How to Execute the code
* Clone first the repository 
* <cd first_mcp/>
* <python client.py>

