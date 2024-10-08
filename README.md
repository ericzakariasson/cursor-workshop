# Cursor Workshop

## Introduction

In this workshop we'll walk through cursor, it's features and how you can leverage it to become more productive.

To demonstrate, we'll be building a simple web app using

- Next.js + ShadCN (and why components are so powerful with Cursor)
- Postgres
- MongoDB

## What's in this repo?

- `prompts/`: shared and version controlled prompts that can be used for your team
- `.cursorrules`: specific Cursor instructions
- `sql/`: small sql scripts for setting up everything related to postgres

## Setup

1. Install docker: Easiest setup is Docker Desktop or OrbStack (my personal preference)
2. Install cursor: https://www.cursor.com/ or `brew install --cask cursor`
3. Install dependencies with `pnpm install` (or remove lockfile and install with npm/yarn/bun)
4. Start the postgres docker container with `pnpm pg:up` and make sure it's running
5. Start the MongoDB docker container with `pnpm mongo:up` and make sure it's running
6. Start the Next.js app with `pnpm dev`

Now, we're ready to start prompting our app.

## Database Management

### PostgreSQL

- Start PostgreSQL: `pnpm pg:up`
- Stop PostgreSQL: `pnpm pg:down`
- Reset PostgreSQL: `pnpm pg:reset`
- Check PostgreSQL status: `pnpm pg:ping`
- Open PostgreSQL shell: `pnpm psql`
- Run SQL tables script: `pnpm pg:tables`

### MongoDB

- Start MongoDB: `pnpm mongo:up`
- Stop MongoDB: `pnpm mongo:down`
- Reset MongoDB: `pnpm mongo:reset`
- Check MongoDB status: `pnpm mongo:ping`
- Open MongoDB shell: `pnpm mongo`

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

## Want to work together?

If you're looking to improve your products, automate processes, or implement AI solutions, let's talk.

- [Website](https://anyblockers.com/consulting)
- [LinkedIn](https://www.linkedin.com/in/ericzakariasson/)
- [Twitter/X](https://twitter.com/ericzakariasson)
