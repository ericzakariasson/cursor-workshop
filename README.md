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
