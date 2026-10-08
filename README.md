# Australian Aboriginal Language Explorer

This project is a small Python web app that reads an Australian Aboriginal language catalogue from a CSV and presents it in a browser-based interface. The app lets you search records, view catalogue status and location summaries, and explore the dataset in a simple interactive UI.

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

4. Install the app's pandas and Matplotlib dependencies:

   ```bash
   python3 -m pip install -r requirements.txt
   ```

## Running the app

From the Assignment folder, run:

```bash
python3 langexpnew.py
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
- Select Data to view record totals, the state/territory bar chart, and the Matplotlib region-count, coordinate-completeness, and location charts.
- Use the search box to quickly filter the table.

The app reads its dataset from `data/pracset.csv`, relative to the project folder. Keep that CSV with the application when sharing or running it.

The app validates that the CSV contains the expected columns before running, so missing or malformed data will stop the app with a clear error message.

## Testing

The project includes eight automated tests covering the data-loading and validation paths, state-counting logic, edge cases, and HTTP routes. Run them from the Assignment folder with:

```bash
python3 -m unittest discover -s tests -v
```

### Syntax check

```bash
python -m py_compile langexpnew.py visualize.py
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

This should print the number of dataset records and confirms the CSV can be read successfully.

## Project files

- `langexpnew.py` — main application entry point with the Data-page charts
- `visualize.py` — Matplotlib chart-building functions
- `requirements.txt` — Python package dependencies
- `data/pracset.csv` — dataset required by the application
- `AI-LOG.md` — assignment notes/log

## Notes

The dataset describes catalogue records rather than current language vitality or community classification. The interface makes that distinction clear in the page text so the app is used responsibly.
