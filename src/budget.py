import json
from pathlib import Path
from datetime import datetime

class BudgetManager:
    def __init__(self, budget_file: str = "budget.json", daily_budget: float = 1.0):
        self.budget_file = Path(budget_file)
        self.daily_budget = daily_budget
        self._load()

    def _load(self):
        if self.budget_file.exists():
            with self.budget_file.open("r", encoding="utf-8") as f:
                self.data = json.load(f)
        else:
            self.data = {}

    def _save(self):
        with self.budget_file.open("w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def add_cost(self, cost: float):
        date_str = datetime.utcnow().strftime("%Y%m%d")
        self.data[date_str] = self.data.get(date_str, 0.0) + cost
        self._save()

    def remaining_budget(self) -> float:
        date_str = datetime.utcnow().strftime("%Y%m%d")
        spent = self.data.get(date_str, 0.0)
        return max(self.daily_budget - spent, 0.0)
