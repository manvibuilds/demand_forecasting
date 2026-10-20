# Demand Forecasting

Forecast weekly product demand for Levi's and The Souled Store from historical sales, so inventory decisions can be made from data instead of guesswork.

The saved forecasts currently cover four Mondays in March 2026: 2, 9, 16, and 23 March. Processed history ends on Monday 23 February 2026. Those March dates stay fixed until the notebooks are run again on newer history.

## Notebooks

1. `notebooks/01_understand_data.ipynb` inspects the original orders.
2. `notebooks/02_levis_sku_category_forecasting.ipynb` builds Levi's weekly SKU and category series.
3. `notebooks/03_souledstore_sku_category_forecasting.ipynb` does the same for The Souled Store.
4. `notebooks/04_machine_learning.ipynb` compares a per-series Random Forest with a repeat-last-week baseline on a chronological 4-week test.
5. `notebooks/05_xgboost_forecasting.ipynb` scores XGBoost on the same features, cutoffs, and horizons, then writes a recursive 4-week forecast.

`docs/project_methodology.md` explains the week alignment, lag features, 20-week history rule, recent-average fallback, and the chronological test. `docs/results_and_analysis.md` records the measured errors, series counts, March 2026 forecasts, and the limitations.

On that test, repeat-last-week is closer for Levi's SKUs. Random Forest has the lower average error for The Souled Store SKUs and categories. XGBoost is not the best method across the four datasets. The Levi's category score uses 2 series and 15 series-cutoff pairs. Many March forecasts use history last observed before 26 January 2026.

## Project layout

```
demand-forecasting/
├── data/
│   ├── raw/          # original CSV files — never edit these
│   └── processed/    # cleaned data written by code
├── notebooks/        # data checks and forecasting notebooks
├── src/              # reusable Python: cleaning, features, models
├── outputs/          # local forecast and evaluation files
├── docs/             # methodology, results, and limitations
├── requirements.txt  # Python libraries
└── README.md
```

Raw files stay untouched. Cleaning and modelling code reads from `data/raw/` and writes results to `data/processed/` and `outputs/`.

Raw order files, processed copies, and the forecast and evaluation CSVs stay on this machine. `.gitignore` leaves them out of Git. A later review would be needed before any of those files are published. The notebooks can still contain printed examples of locations, items, and quantities in their saved cell outputs.

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
- Do not commit or publish raw data, processed data, forecast CSVs, or evaluation CSVs unless that publication has been reviewed separately.
