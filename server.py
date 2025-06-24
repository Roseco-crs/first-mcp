from fastmcp import FastMCP, Client
import asyncio

mcp = FastMCP("First MCP Server")

@mcp.tool()
def greet(name: str) -> str:
    """ Greet a user by name."""
    return f"Hello, {name}!" 

# greet.enable()
# greet.disable()

# we use mpc.run to execute the MCP server
if __name__ == "__main__":
    # mcp.run()
    mcp.run(transport="stdio")


# from typing import Annotated, Optional
# from pydantic import Field, BaseModel
# class Users(BaseModel):
#     name: str
#     eamil: str = Field(description="Email of the user")
#     age: Optional[int] = Field(default= None, description="Age of the user")
#     # age: int | None = None      # Optional[int]
#     is_active: bool = True


 

    