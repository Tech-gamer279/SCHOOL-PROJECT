# Alien Invasion

Alien Invasion is a Pygame game in which you move a rocket ship with the arrow
keys and shoot aliens with the spacebar.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m pygbag --ume_block 0 .
```

Open the local URL printed by pygbag, usually `http://127.0.0.1:8000`.

## Publish online

Push the repository to GitHub and enable **Settings > Pages > Source: GitHub
Actions**. Every push to `main` then builds and deploys the game. The shareable
URL is shown in the workflow run and will normally be:

`https://<your-github-username>.github.io/<repository-name>/`