import os
from slack_sdk.webhook import WebhookClient

class SlackNotifier:
    def __init__(self, webhook_url: str | None = None):
        self.webhook_url = webhook_url or os.getenv("SLACK_WEBHOOK_URL")
        self.client = WebhookClient(self.webhook_url)

    async def send(self, text: str):
        if not self.webhook_url:
            return
        self.client.send(text=text)
