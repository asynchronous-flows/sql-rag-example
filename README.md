<div align="center">
<h1>
SQL RAG Example
</h1>

Built with `asyncflows`

[![main repo](https://img.shields.io/badge/main_repo-1f425f)](https://github.com/asynchronous-flows/asyncflows)
[![Discord](https://img.shields.io/badge/discord-7289da)](https://discord.gg/AGZ6GrcJCh)

</div>

## Introduction

This example demonstrates asking questions about a SQL database, and answering them with the results of generated SQL queries.

<div align="center">
</div>

## Running the Example

To run the example:

1. Set up [Ollama](https://github.com/asynchronous-flows/asyncflows#setting-up-ollama-for-local-inference) or configure [another language model](https://github.com/asynchronous-flows/asyncflows#using-any-language-model)  

2. Clone the repository

```bash
git clone ssh://git@github.com/asynchronous-flows/sql-rag-example
```

3. Change into the directory

```bash
cd sql-rag-example
```

4. Create and activate your virtual environment (with, for example)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

5. Install the dependencies

```bash
pip install -r requirements.txt
```

6. Run the example

```bash
python sql_rag.py
```

## Using your own Data

To use your own data, set the `DATABASE_URL` environment variable (e.g., `export DATABASE_URL=sqlite:///my-database.db`).

If you'd like to use a database other than sqlite (e.g., postgres),
install the [corresponding asyncflows dependency](https://github.com/asynchronous-flows/asyncflows#sql-databases) (e.g., `pip install asyncflows[pg]`).
