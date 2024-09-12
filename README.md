# Cursor Workshop

## Introduction

In this workshop we'll walk through cursor, it's features and how you can levarage it to become more productive.

To demonstrate, we'll be building a simple web app using

- Next.js + ShadCN (and why components are so powerful with Cursor)
- Postgres

## What's in this repo?

- `prompts/`: shared and version controlled prompts that can be used for your team
- `.cursorrules`: specific Cursor instructions
- `sql/`: small sql scripts for seting up everything related to postgres

## Setup

1. Install docker: Easiest setup is Docker Desktop or OrbStack (my personal preference)
2. Install cursor: https://www.cursor.com/ or `brew install --cask cursor`
3. Install dependencies with `pnpm install` (or remove lockfile and install with npm/yarn/bun)
4. Start the postgres docker container with `pnpm db:up` and make sure it's running
5. Start the Next.js app with `pnpm dev`

Now, we're ready to start prompting our app.

## Other tools

- [warp.dev terminal](https://www.warp.dev/): terminal with built in completion capabilities
- [LLM cli](https://llm.datasette.io/en/stable/): cli tool to call LLMs directly in the terminal
  - Can be used together with [this snippet](https://gist.github.com/karpathy/1dd0294ef9567971c1e4348a90d69285) to automatically generate commit messages
- [Ollama](https://ollama.com/): run LLMs locally (cli)
- [LM Studio](https://lmstudio.ai/): run and visualise LLMs locally (gui)
- [Ellipsis](https://www.ellipsis.dev/): automated code review in GitHub PRs
- [Cursor Directory](https://cursor.directory/): a collection of prompts and .cursorrules files
- [Cursor Lens](https://www.cursorlens.com/): Cursor analytics

## Stay updated

I share learnings from the field, tips and tricks on [anyblockers.com](https://anyblockers.com/)
