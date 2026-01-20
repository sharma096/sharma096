import requests

MCP_URL = "http://127.0.0.1:8000/mcp"

def call_mcp_tool(tool_name: str, payload: dict):
    response = requests.post(
        f"{MCP_URL}/tools/{tool_name}",
        json=payload,
        timeout=600
    )
    response.raise_for_status()
    return response.json()
