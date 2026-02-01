# Store (Archived) — Minimal Inventory + SQLite Demo

A small, modular Python project that demonstrates a simple inventory management flow backed by SQLite.

This repo is intentionally **basic** and is now **archived** (kept as a reference / learning artifact). It’s useful as a compact example of:
- a domain model (`Product`)
- an inventory manager (`Inventory`)
- a SQLite persistence layer (create/seed/query/update)
- a simple interactive CLI loop

## Features
- **SQLite database initialization + seeding**
  - Creates a `products` table on first run and seeds a handful of example products.
- **Inventory view**
  - Prints a formatted inventory table in the terminal.
- **Stock updates**
  - Add stock to a product (updates in memory + persists to SQLite).
- **Modular structure**
  - `models/`, `db/`, `utils/`, plus a CLI entry point.
```text
## Project layout
Store/
├── main.py
├── config.py
├── api/
│ └── client.py
├── db/
│ └── database.py
├── models/
│ ├── inventory.py
│ └── product.py
└── utils/
└── formatter.py
```

### Notes on architecture (why it looks like this)
This repo went through a “demo evolution”:
- `api/client.py` simulates fetching product data from an external API.
- The current app flow primarily uses **SQLite** (`db/database.py`) as the data source.
- `config.py` includes both a simple constant and a more structured config class approach.

That inconsistency is intentional for an archived learning repo: it shows two common directions a project can go.

## Requirements
- Python 3.9+ (works on typical modern Python 3 versions)
- No external dependencies required for core functionality (SQLite is part of Python’s stdlib)

> `requests` is imported in the API simulation module, but the main program does not require it.

## Quick start
Clone and run:

```bash
python main.py
```
On first run, the program will:

1. Create a local SQLite DB (development config)
2. Create the products table if missing
3. Seed initial products
4. Launch the interactive CLI

### How it works (high level)
- main.py drives a basic menu loop:
  - refresh inventory from DB
  - add stock to a product

- Inventory loads products from the DB into an in-memory dictionary keyed by product_id.
- Stock updates:

1. update the Product object in memory
2. persist the new stock value to SQLite
3. if the DB write fails, revert the in-memory stock

### Configuration
The configuration is intentionally simple and demo-friendly.

By default, it uses a development configuration which points to a local SQLite file.

You can switch config selection via:

- APP_ENV=production (uses the ProductionConfig)
- otherwise defaults to development

Example (Windows PowerShell):

```powershell
$env:APP_ENV="development"
python main.py
```
Example (bash):
```bash
APP_ENV=development python main.py
```
## Limitations (by design)
Because this is an archived reference repo, some things are intentionally not “production ready”:

- Minimal error handling and no logging framework
- No unit tests included
- Simple CLI (no rich UI)
- DB URI parsing assumes sqlite:///... format

Possible extensions (if you ever revive it)
Add unit tests for DB init, inventory load, and stock updates

- Add “remove stock” / “create product” / “delete product”
- Replace the CLI refresh loop with a structured command system (argparse / typer)
- Unify configuration style (either constants or Config classes)
- Add migrations (Alembic-style concept, even if staying on SQLite)

### License
Unlicensed / personal archive by default.
