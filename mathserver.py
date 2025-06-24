from fastmcp import FastMCP, Context
from typing import Optional, Union, Literal, List, Tuple, Dict, Any

mcp = FastMCP(name="Math MCP Server")

@mcp.tool()
def division(a: Union[float, int], b: Union[float, int]) -> Union[float, int]:
    """Divide two numbers to each other."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Invalid types: {type(a)} and {type(b)}. Both must be int or float.")
    return a/b

@mcp.tool()
def modulo(a: int | float, b: int | float) -> int | float:
    """ Modulo or remaining of a divided by b."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"Invalid types: {type(a)} and {type(b)}. Both must be int or float.")
    return a%b

if __name__ == "__main__":
    mcp.run(transport="stdio")

# Modern Python syntax (str | int) is preferred over older Union[str, int] forms. 
# Similarly, str | None is preferred over Optional[str].