import os
import json
import httpx
from typing import Any

class APIRouter:
    def __init__(self, routes_path: str = "routes.json"):
        with open(routes_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.default = data.get("default")
        self.routes = data["routes"]

    async def call(self, provider: str | None, endpoint: str, payload: dict) -> Any:
        key = provider or self.default
        info = self.routes[key]
        api_key = os.getenv(info["api_key_env"], "")
        url = f"{info['base_url'].rstrip('/')}/{endpoint.lstrip('/')}"
        headers = {"Authorization": f"Bearer {api_key}"}
        async with httpx.AsyncClient(timeout=30) as client:
            resp = await client.post(url, json=payload, headers=headers)
            resp.raise_for_status()
            return resp.json()
