# Kuu Core Lite Setup

This repository provides a minimal asynchronous framework for the Kuu structured AI.
It focuses on low-resource environments and separates heavy tasks into modules.

## Directory Layout

```
.
├── config.yaml
├── routes.json
├── .env.sample
├── src/
│   ├── api_router.py
│   ├── budget.py
│   ├── logger.py
│   ├── main.py
│   └── slack_notifier.py
├── logs/
├── memory/
├── datasets/
```

## Usage

1. Copy `.env.sample` to `.env` and fill API keys and Slack webhook.
2. Adjust `config.yaml` and `routes.json` as needed.
3. Run `python src/main.py` to execute a sample request via the router.

## Memory & CPU Tips

- Keep daily budget small in `.env` to avoid long-running sessions.
- Heavy tasks such as LoRA or image processing should be placed in separate async
  workers that run only when resources allow.
- Monitor `memory/` and `datasets/` sizes and prune old data regularly.

