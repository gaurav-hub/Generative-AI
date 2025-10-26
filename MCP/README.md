# MathMCP Tools

This folder contains a Model Context Protocol (MCP) server implementation for mathematical operations.

## Files

- `mathserver.py`: An MCP server using FastMCP that provides tools for basic math operations, such as adding and multiplying numbers. It runs with stdio transport.

## How to Run

1. Install dependencies: `pip install mcp`.
2. Run the MCP server: `python mathserver.py`.
3. The server will start and listen for stdio input/output for MCP protocol communication.
4. Use an MCP client to connect and invoke the math tools (add, multiply).
