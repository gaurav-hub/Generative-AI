"""
MathMCP Tools Server

This module implements a Model Context Protocol (MCP) server using FastMCP for basic mathematical operations.

Functions:
    add(a, b): Adds two numbers.
    multiply(a: int, b: int) -> int: Multiplies two integers.

Usage:
    Run this script to start the MCP server with stdio transport.
"""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Match")

@mcp.tool()
def add(a, b):
    """
    Adds two numbers.

    Args:
        a: First number.
        b: Second number.

    Returns:
        The sum of a and b.
    """
    return a + b

@mcp.tool
def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The product of a and b.
    """
    return a * b

if __name__ == "__main__":
    mcp.run(transport="stdio")
