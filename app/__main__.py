#!/usr/bin/env python
"""Entry point for running Hass-MCP as a module"""

from app.server import mcp


def main():
    """Run the MCP server with treamable-http communication"""
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)


if __name__ == "__main__":
    main()