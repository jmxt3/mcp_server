from fastmcp import FastMCP
import asyncio

mcp = FastMCP(name="MyServer")


@mcp.tool()
def hello(name: str) -> str:
    return f"Hello, {name}!"


async def main():
    # Use run_async() in async contexts
    await mcp.run_async(transport="streamable-http")


if __name__ == "__main__":
    asyncio.run(main())
