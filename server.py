import os
from fastmcp import FastMCP

mcp = FastMCP("Calculadora MCP Básica")

@mcp.tool(name="sumar")
def sumar(a: float, b: float) -> float:
    return a + b

@mcp.tool(name="restar")
def restar(a: float, b: float) -> float:
    return a - b

if __name__ == "__main__":
    # Usa el puerto que Render asigna automáticamente
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="http", host="0.0.0.0", port=port)
