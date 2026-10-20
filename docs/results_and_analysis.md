# Results and analysis

These figures come from the notebook 5 run on 20 October 2026. The method is described in `docs/project_methodology.md`. This file first records what was measured, then lists limitations and assumptions separately.

## What was measured

XGBoost was scored on the same eight cutoffs used for Random Forest, 2025-12-08 through 2026-01-26, and on the same series-cutoff pairs. Repeat-last-week error was recomputed and matched `outputs/ml_rolling_origin_evaluation.csv` at every horizon before the comparison was saved. Random Forest was not trained again. Its MAE and median absolute error are the values already stored in that file.

MAE is the average absolute error in units. Median AE is the absolute error of the typical scored week, also in units.

## Series included and excluded

A series enters the score only when it can be evaluated at one or more cutoffs. Exclusion does not remove the series from the March forecast file.

| Dataset | Series in the data | Series scored | Series excluded | Excluded, history shorter than 20 weeks | Excluded, 20 or more weeks but a cutoff or future week was missing | Series-cutoff pairs |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Levi's SKU | 353 | 41 | 312 | 204 | 108 | 224 |
| Souled Store SKU | 1,127 | 227 | 900 | 773 | 127 | 1,461 |
| Levi's category | 32 | 2 | 30 | 30 | 0 | 15 |
| Souled Store category | 199 | 76 | 123 | 91 | 32 | 528 |

The skip counts below are cutoff attempts, not series. Each series is considered at eight cutoffs, so the counts are larger than the number of series.

| Dataset | Cutoff attempts skipped because history was still under 20 weeks | Cutoff attempts skipped because that week is absent | Cutoff attempts skipped because one of the next four weeks is absent |
| --- | ---: | ---: | ---: |
| Levi's SKU | 226 | 2,238 | 136 |
| Souled Store SKU | 2,387 | 4,940 | 228 |
| Levi's category | 23 | 217 | 1 |
| Souled Store category | 431 | 577 | 56 |

## Accuracy by dataset and horizon

The lowest-MAE and lowest-median columns name every method that shares the best value after rounding to two decimals.

### All four weeks

| Dataset | Scored weeks | XGBoost MAE | Random Forest MAE | Repeat last week MAE | XGBoost median AE | Random Forest median AE | Repeat last week median AE | Lowest MAE | Lowest median AE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Levi's SKU | 896 | 6.93 | 7.24 | 4.08 | 0.89 | 1.73 | 0.00 | Repeat last week | Repeat last week |
| Souled Store SKU | 5,844 | 6.23 | 5.59 | 5.97 | 2.03 | 1.90 | 2.00 | Random Forest | Random Forest |
| Levi's category | 60 | 1,263.64 | 1,270.06 | 1,742.63 | 126.32 | 174.52 | 44.00 | XGBoost | Repeat last week |
| Souled Store category | 2,112 | 13.94 | 12.63 | 13.43 | 2.32 | 2.00 | 2.00 | Random Forest | Tie: Random Forest and repeat last week |

### One week ahead

| Dataset | XGBoost MAE | Random Forest MAE | Repeat last week MAE | XGBoost median AE | Random Forest median AE | Repeat last week median AE | Lowest MAE | Lowest median AE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Levi's SKU | 7.17 | 7.33 | 4.70 | 0.98 | 1.59 | 0.00 | Repeat last week | Repeat last week |
| Souled Store SKU | 4.90 | 4.37 | 4.55 | 1.84 | 1.76 | 1.00 | Random Forest | Repeat last week |
| Levi's category | 1,210.87 | 1,191.95 | 1,146.87 | 93.44 | 60.62 | 18.00 | Repeat last week | Repeat last week |
| Souled Store category | 10.20 | 9.19 | 9.52 | 2.24 | 1.89 | 2.00 | Random Forest | Random Forest |

### Two weeks ahead

| Dataset | XGBoost MAE | Random Forest MAE | Repeat last week MAE | XGBoost median AE | Random Forest median AE | Repeat last week median AE | Lowest MAE | Lowest median AE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Levi's SKU | 6.80 | 6.90 | 4.65 | 0.66 | 1.60 | 0.00 | Repeat last week | Repeat last week |
| Souled Store SKU | 5.99 | 5.41 | 5.56 | 2.00 | 1.91 | 2.00 | Random Forest | Random Forest |
| Levi's category | 1,301.23 | 1,276.03 | 1,928.87 | 268.79 | 342.42 | 35.00 | Random Forest | Repeat last week |
| Souled Store category | 13.45 | 11.94 | 12.96 | 2.32 | 2.02 | 2.00 | Random Forest | Repeat last week |

### Three weeks ahead

| Dataset | XGBoost MAE | Random Forest MAE | Repeat last week MAE | XGBoost median AE | Random Forest median AE | Repeat last week median AE | Lowest MAE | Lowest median AE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Levi's SKU | 6.91 | 7.52 | 3.89 | 0.74 | 1.83 | 0.00 | Repeat last week | Repeat last week |
| Souled Store SKU | 6.92 | 6.21 | 6.72 | 2.20 | 2.00 | 2.00 | Random Forest | Tie: Random Forest and repeat last week |
| Levi's category | 1,303.22 | 1,279.42 | 1,989.13 | 93.46 | 544.44 | 205.00 | Random Forest | XGBoost |
| Souled Store category | 16.25 | 14.41 | 15.74 | 2.33 | 2.00 | 2.00 | Random Forest | Tie: Random Forest and repeat last week |

### Four weeks ahead

| Dataset | XGBoost MAE | Random Forest MAE | Repeat last week MAE | XGBoost median AE | Random Forest median AE | Repeat last week median AE | Lowest MAE | Lowest median AE |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| Levi's SKU | 6.83 | 7.22 | 3.09 | 1.00 | 2.16 | 0.00 | Repeat last week | Repeat last week |
| Souled Store SKU | 7.12 | 6.37 | 7.03 | 2.26 | 2.01 | 2.00 | Random Forest | Repeat last week |
| Levi's category | 1,239.25 | 1,332.85 | 1,905.67 | 319.96 | 542.29 | 258.00 | XGBoost | Repeat last week |
| Souled Store category | 15.86 | 14.97 | 15.50 | 2.49 | 2.17 | 3.00 | Random Forest | Random Forest |

On individual scored weeks, repeat-last-week is closer than XGBoost more often in every dataset. Over all four weeks the counts are:

| Dataset | XGBoost closer | Repeat last week closer | Ties |
| --- | ---: | ---: | ---: |
| Levi's SKU | 181 | 592 | 123 |
| Souled Store SKU | 2,524 | 3,114 | 206 |
| Levi's category | 21 | 38 | 1 |
| Souled Store category | 972 | 1,096 | 44 |

## What the scores support

XGBoost is not the best method across this test.

- Levi's SKUs: repeat-last-week has the lower average error and the lower typical-week error at every horizon. Many of those SKUs stay at the same weekly demand, so the typical baseline error is 0. XGBoost's average error (6.93) is a little lower than Random Forest (7.24). Both remain above repeat-last-week (4.08).
- Souled Store SKUs: Random Forest has the lowest average error over all four weeks (5.59), then repeat-last-week (5.97), then XGBoost (6.23). Random Forest also has the lowest typical-week error (1.90).
- Levi's categories: over all 60 scored weeks, XGBoost has a slightly lower average error than Random Forest (1,263.64 versus 1,270.06). Both are lower than repeat-last-week (1,742.63). The typical week is closer under repeat-last-week (median 44.00, versus 126.32 for XGBoost). This row is 15 series-cutoff pairs from 2 series. At one week ahead, repeat-last-week has the lowest average error.
- Souled Store categories: Random Forest has the lowest average error at every horizon. Over all four weeks its MAE is 12.63, repeat-last-week is 13.43, and XGBoost is 13.94. The typical-week error is 2.00 for both Random Forest and repeat-last-week, and 2.32 for XGBoost.

## March forecasts

The forecast files currently cover March 2026 only. Every series in the processed data has a forecast for 2026-03-02, 2026-03-09, 2026-03-16, and 2026-03-23. History ends on 2026-02-23, so these four weeks are the horizon after the last observed week. They do not move forward on their own. No saved forecast is negative. None is above that series' own historical maximum. Validation of the four files passed.

| Dataset | Rows | XGBoost series | Recent-average series | Minimum | Maximum |
| --- | ---: | ---: | ---: | ---: | ---: |
| Levi's SKU | 1,412 | 149 | 204 | 0.00 | 1,067.75 |
| Souled Store SKU | 4,508 | 354 | 773 | 0.00 | 131.13 |
| Levi's category | 128 | 2 | 30 | 0.00 | 5,735.89 |
| Souled Store category | 796 | 108 | 91 | 0.00 | 491.19 |

The 20-week split matches notebook 4: the same series that used Random Forest now use XGBoost, and the same short series use the recent-average fallback.

History freshness, using the last observed week on each series:

| Dataset | Observed on 2026-02-23 | Recent, from 2026-01-26 but not the final week | Stale, last observed before 2026-01-26 |
| --- | ---: | ---: | ---: |
| Levi's SKU | 40 | 95 | 218 |
| Souled Store SKU | 211 | 325 | 591 |
| Levi's category | 8 | 22 | 2 |
| Souled Store category | 77 | 56 | 66 |

Two Levi's category examples show how a per-series forecast behaves:

- South Warehouse jeans has 82 weeks, including recent weeks of 6,488, 1,466, 354, and 21, and a historical maximum of 9,993. Its XGBoost forecast is 526.31, 5,735.89, 574.35, and 857.88. The second week is large because that demand is in this series' own history. It stays below the series maximum.
- North Warehouse jeans has recent weeks of 2, 1, 5, and 7, and a historical maximum of 401. Its XGBoost forecast is 0.00, 0.00, 16.08, and 30.76. It does not copy the South Warehouse level. By the third and fourth weeks it has moved away from the last four actual weeks.

The largest Levi's SKU forecast, 1,067.75, is the recent-average fallback, the same value notebook 4 reported for a short South Warehouse SKU.

## Runtime

Timed inside the successful notebook run:

| Step | Seconds |
| --- | ---: |
| Eight recursive forecasts in the sanity test | 0.28 |
| Check that cutoffs and repeat-last-week errors match the saved Random Forest file | 0.94 |
| Full XGBoost evaluation, 2,228 series-cutoff models | 54.70 |
| March forecasts for all series | 19.73 |

The whole notebook execution in the project virtual environment took about 93 seconds. An earlier attempt to execute it with the default Jupyter kernel stopped on the import, because that kernel's Python did not have XGBoost installed. The completed run used the project virtual environment, where XGBoost 3.2.0 is installed. The completed run itself reported no cell errors.

## Files written

- `notebooks/05_xgboost_forecasting.ipynb`
- `outputs/xgboost_model_evaluation.csv`
- `outputs/model_comparison.csv`
- `outputs/levis_sku_xgboost_forecast.csv`
- `outputs/souledstore_sku_xgboost_forecast.csv`
- `outputs/levis_category_xgboost_forecast.csv`
- `outputs/souledstore_category_xgboost_forecast.csv`
- `docs/project_methodology.md`
- `docs/results_and_analysis.md`
- `requirements.txt` gained one line, `xgboost==3.2.0`

Notebooks 1 to 4, the raw data, the processed data, and the earlier output files were not replaced.

## Limitations and assumptions

These points are not extra measurements. They bound how the numbers above should be read.

- The XGBoost settings were fixed in advance. No search over learning rate, tree count, or depth was run, so a different setting could score differently.
- Random Forest errors are the saved rolling-origin results. They were not recomputed in this run. The match of cutoff dates, pair counts, and repeat-last-week MAE and median AE is the evidence that the eligible weeks are the same.
- Week-by-week win counts are between XGBoost and repeat-last-week only. The saved Random Forest file does not contain each week's prediction, so a week-by-week count against Random Forest is not available.
- Levi's category accuracy rests on 2 series and 15 series-cutoff pairs. A small MAE gap there, such as 1,263.64 versus 1,270.06, is a thin basis for preferring one model.
- Average error on Levi's categories is large because the scored history includes South Warehouse weeks of several thousand units. Median absolute error is the better description of a typical week.
- Most series are outside the accuracy table. Short series are forecast with a flat recent average. Long series that miss the cutoff week, or miss one of the next four observed weeks, are forecast for March but are not part of the score.
- Many March forecasts use stale history. For Levi's SKUs, 218 of 353 series were last observed before 2026-01-26. Those forecasts describe older demand.
- The recursive step feeds predictions forward. Error can grow or jump from one future week to the next, as in the South Warehouse jeans forecast above. The test measures that recursive path. It is a harder test than the one-step holdout in `outputs/ml_model_evaluation.csv`.
- Lags follow stored rows. Where a category series skips a week, `lag_1` can be more than one calendar week earlier. Missing weeks were not filled with zero.
- Large historical weeks were kept. The thousand-unit South Warehouse weeks may be real warehouse volume or a unit-definition question. This run does not resolve that business question.
- No commit, push, or data publication was made.
