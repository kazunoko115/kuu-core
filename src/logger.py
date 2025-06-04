import os
import json
from datetime import datetime
from pathlib import Path

class DailyLogger:
    def __init__(self, log_dir: str = "logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

    @property
    def _log_path(self) -> Path:
        date_str = datetime.utcnow().strftime("%Y%m%d")
        return self.log_dir / f"kuu_log_{date_str}.json"

    def append(self, entry: dict):
        path = self._log_path
        data = []
        if path.exists():
            with path.open("r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        data.append(entry)
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
