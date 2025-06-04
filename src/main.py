import asyncio
import os
from logger import DailyLogger
from budget import BudgetManager
from slack_notifier import SlackNotifier
from api_router import APIRouter

logger = DailyLogger()
budget = BudgetManager(daily_budget=float(os.getenv("DAILY_BUDGET", 1.0)))
slack = SlackNotifier()
router = APIRouter()

async def run_task():
    # example payload
    payload = {"messages": [{"role": "user", "content": "Hello"}]}
    if budget.remaining_budget() <= 0:
        await slack.send("Budget exceeded")
        return
    response = await router.call(None, "chat/completions", payload)
    logger.append(response)
    cost = response.get("usage", {}).get("total_tokens", 0) * 0.000002  # example cost
    budget.add_cost(cost)
    await slack.send("Task completed")

if __name__ == "__main__":
    asyncio.run(run_task())
