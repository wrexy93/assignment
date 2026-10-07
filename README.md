# Australian Aboriginal Language Explorer

This project is a small Python web app that loads a CSV dataset of Australian Aboriginal language records and presents it in a browser-based interface. The app lets you search records, view catalogue status and location summaries, and explore the supplied dataset in a simple interactive UI.

## Installation

1. Open a terminal in the project directory:

   ```bash
   cd /path/to/CITS1501/Assignment
   ```

2. Create and activate a virtual environment if you want an isolated setup:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Confirm Python is available:

   ```bash
   python --version
   ```

4. No extra packages are required for the app itself because it uses the Python standard library only.

## Running the app

From the Assignment folder, run:

```bash
python langexp.py
```

This starts a local HTTP server and opens the app in your default browser automatically. The terminal will display the local URL, usually in the form:

```text
http://127.0.0.1:PORT/
```

Press Ctrl+C in the terminal to stop the server.

## Usage

Once the app is running:

- Open the Home page to see a summary of the dataset.
- Select Explore Languages to search the catalogue by language name, code, state/territory, or status.
- Select Data to view record totals and summary statistics.
- Use the search box to quickly filter the table.

The app reads the dataset from:

```text
./data/pracset.csv
```

It validates that the CSV contains the expected columns before running, so missing or malformed data will stop the app with a clear error message.

## Testing

This project does not currently include a formal automated test suite, but you can still run a quick verification to make sure the app starts cleanly.

### Syntax check

```bash
python -m py_compile langexp.py
```

This checks that the Python file has valid syntax.

### Basic smoke test

Run the app and confirm that:

- the terminal prints a local URL,
- the browser opens,
- the page loads without errors,
- the search and data summary render using the supplied CSV.

If you want to do a simple import-level validation from the terminal:

```bash
python - <<'PY'
from pathlib import Path
import langexp
records = langexp.load_records(Path('data/pracset.csv'))
print(f"Loaded {len(records)} records")
PY
```

This should print the number of loaded dataset records and confirms the CSV can be read successfully.

## Project files

- `langexp.py` — main application entry point
- `data/pracset.csv` — source dataset used by the explorer
- `AI-LOG.md` — assignment notes/log

## Notes

The dataset describes catalogue records rather than current language vitality or community classification. The interface makes that distinction clear in the page text so the app is used responsibly.
