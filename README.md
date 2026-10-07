# Australian Aboriginal Language Explorer

This project is a small Python web app that includes a bundled copy of an Australian Aboriginal language catalogue and presents it in a browser-based interface. The app lets you search records, view catalogue status and location summaries, and explore the dataset in a simple interactive UI.

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

4. Install the app's pandas dependency:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

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
- Select Data to view record totals, summary statistics, and a bar chart of distinct catalogue language names by state or territory.
- Use the search box to quickly filter the table.

The dataset is bundled in `embedded_data.py`. Keep `langexp.py` and `embedded_data.py` together when sharing or running the application. The CSV in `data/pracset.csv` is retained as the source copy but is not required at runtime.

The app validates that the bundled CSV contains the expected columns before running, so missing or malformed data will stop the app with a clear error message.

## Testing

The project includes eight automated tests covering the data-loading and validation paths, state-counting logic, edge cases, and HTTP routes. Run them from the Assignment folder with:

```bash
python3 -m unittest discover -s tests -v
```

### Syntax check

```bash
python -m py_compile langexp.py embedded_data.py
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
import langexp
records = langexp.load_records()
print(f"Loaded {len(records)} records")
PY
```

This should print the number of bundled dataset records and confirms the data can be read successfully.

## Project files

- `langexp.py` — main application entry point
- `embedded_data.py` — compressed dataset bundled with the application
- `requirements.txt` — Python package dependencies
- `data/pracset.csv` — source copy of the dataset; not needed to run the app
- `AI-LOG.md` — assignment notes/log

## Notes

The dataset describes catalogue records rather than current language vitality or community classification. The interface makes that distinction clear in the page text so the app is used responsibly.
