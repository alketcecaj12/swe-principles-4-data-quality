# Data Quality Toolkit

A small, well-tested Python package for cleaning tabular data before it reaches analysis or modelling. It's built on pandas and structured as an installable package with a command-line entry point and an automated test suite.

## Features

- **Missing-value removal**: drops incomplete rows from a `DataFrame` and returns a new copy, so the input data is never modified.
- **Command-line interface**: runs the cleaning pipeline from the terminal with a single command.
- **Typed, documented functions**: each transformation has type hints and a docstring describing its contract.
- **Test coverage**: every transformation is covered by unit tests run with pytest.

## Project structure

```
.
├── src/
│   └── churn/
│       ├── __init__.py
│       ├── cli.py            # Command-line entry point
│       └── preprocessing.py  # Data-cleaning functions
├── tests/
│   └── test_preprocessing.py # Unit tests for preprocessing
├── pyproject.toml            # Package metadata, dependencies, CLI script
└── README.md
```

The project uses the **`src/` layout**: the package lives under `src/`, so tests always run against the installed package rather than files that happen to be on the path.

## Requirements

- Python 3.11 or newer
- pandas 2.0 or newer (installed automatically)

## Installation

Clone the repository and install it in editable mode with the development dependencies:

```bash
git clone https://github.com/alketcecaj12/swe-principles-4-data-quality.git
cd swe-principles-4-data-quality
python -m venv .venv
```

Activate the virtual environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

Then install:

```bash
python -m pip install -e ".[dev]"
```

## Usage

### From the command line

```bash
churn
```

This runs the cleaning step on a small sample dataset and prints the result:

```
    age  monthly_spend
0  25.0             50
1  30.0             80
```

The third row, which had a missing `age`, has been removed.

### As a library

```python
import pandas as pd

from churn.preprocessing import remove_missing_values

df = pd.DataFrame({
    "age": [25, None, 40],
    "spend": [100, 200, 300],
})

clean = remove_missing_values(df)
# `df` is unchanged; `clean` contains only complete rows
```

## Running the tests

```bash
python -m pytest -q
```

## Design principles

- **Pure functions**: transformations take a `DataFrame` and return a new one, with no side effects on their input.
- **Separation of concerns**: data logic lives in `preprocessing.py`; input/output and orchestration live in `cli.py`.
- **Declarative packaging**: dependencies, optional dev tools and the CLI entry point are all defined in `pyproject.toml`.
- **Test-first confidence**: each public function is covered by tests before it's relied on elsewhere.

## Roadmap

- [ ] Read input from CSV / Parquet files instead of the built-in sample
- [ ] Configurable cleaning rules (per-column thresholds, imputation strategies)
- [ ] Schema and range validation with clear error reporting
- [ ] Data-quality summary report (missingness, duplicates, outliers)
- [ ] Linting, formatting and type checking (ruff, mypy)
- [ ] Continuous integration with GitHub Actions
