# Demand Forecasting

Forecast product demand from historical sales so inventory decisions can be made from data instead of guesswork.

## Project layout

```
demand-forecasting/
├── data/
│   ├── raw/          # original CSV files — never edit these
│   └── processed/    # cleaned data written by code
├── notebooks/        # exploration (Step 1)
├── src/              # reusable Python: cleaning, features, models
├── outputs/          # charts and forecast files
├── requirements.txt  # Python libraries
└── README.md
```

Raw files stay untouched. Cleaning and modelling code reads from `data/raw/` and writes results to `data/processed/` and `outputs/`.

## Setup

From the project folder:

```bash
python -m venv .venv
```

Activate the environment:

- Windows (PowerShell): `.venv\Scripts\Activate.ps1`
- macOS / Linux: `source .venv/bin/activate`

Install libraries:

```bash
pip install -r requirements.txt
```

## How to run

1. Copy the two original CSV files into `data/raw/`. Do not edit them.
2. Start Jupyter for exploration:

```bash
jupyter notebook
```

3. Open notebooks from the `notebooks/` folder. Save cleaned data to `data/processed/` and charts or forecast files to `outputs/`.
4. Put reusable functions (cleaning, features, models) in `src/` so notebooks stay thin and the same code can be rerun.

## Rules

- Never modify files in `data/raw/`.
- Generate `data/processed/` and `outputs/` from code so the project can be rerun from the original files.
