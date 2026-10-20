# Project methodology

This note describes how the Levi's and The Souled Store demand forecasts were built in notebooks 4 and 5. It describes the data rules, the models, and the test. The measured scores are in `docs/results_and_analysis.md`.

## Question

For each fulfilment location and item, how many units should be expected in each of the next four weeks?

An item is a SKU in the SKU files and a category in the category files. The forecast is weekly.

## Data

The models read four processed weekly files and do not change them:

| Dataset | File |
| --- | --- |
| Levi's SKU | `data/processed/levis_Order_data_cleaned_weekly_filled.csv` |
| Souled Store SKU | `data/processed/thesouledstore_Oder_data_cleaned_weekly_filled.csv` |
| Levi's category | `data/processed/levis_category_weekly.csv` |
| Souled Store category | `data/processed/souledstore_category_weekly.csv` |

Files in `data/raw/` stay untouched. Notebook 5 also leaves the processed files untouched.

Each row is one location, one item, and one week, with `Net Sold Quantity`. After the week labels are aligned, every dataset runs from a Monday start date through Monday 2026-02-23. There are no missing values, no negative quantities, and no duplicate location-item-week rows in these files.

## Week labels

SKU weeks are already Mondays. Category weeks are Tuesdays. A Tuesday category label is the day after the Monday used for the same week in the SKU files. Category dates are moved back one day. For example, category week 2026-02-24 is the same week as SKU week 2026-02-23.

The move changes the label only. Quantity is unchanged, and no rows are added or removed. Levi's category demand stays 124,240. Souled Store category demand stays 75,820.

## Features

A model predicts a week from demand already stored for that same location and item:

- `lag_1` is the previous stored week
- `lag_2` is two stored weeks earlier
- `lag_4` is four stored weeks earlier
- `rolling_mean_4` is the average of those previous four stored weeks

The week being predicted is not one of its own inputs. In the filled SKU files, stored weeks are consecutive Mondays. A category series can skip a week. A missing week is left missing. It is not filled with zero in notebook 5. The lag is then the previous stored observation, which may be more than seven days earlier. That is the same rule notebook 4 uses.

## Short histories

XGBoost and Random Forest are trained only when a series has at least 20 stored weeks. The first four weeks create the lags, so 20 weeks leave 16 training rows.

A shorter series keeps the recent-average fallback from notebook 4. The forecast is the average of the last four stored weeks when those weeks exist, and otherwise the average of every stored week. The same number is used for all four future weeks and labeled `recent_average_fallback`. No historical week is invented.

## Models

Notebook 4 fits a separate Random Forest for each long series: 100 trees, depth at most 4, at least 5 historical weeks in each leaf, and `random_state=42`.

Notebook 5 fits a separate XGBoost model for each long series. The settings were chosen before the scores were read, and they were not searched on the holdout:

- 100 trees
- maximum depth 4
- `min_child_weight=5`, so a leaf covers at least 5 training rows under squared error
- learning rate 0.1
- `random_state=42`
- one processor per model

Predictions below zero are raised to zero.

Random Forest is not trained again in notebook 5. Its published errors are taken from `outputs/ml_rolling_origin_evaluation.csv` after a check that the eligible series, cutoff dates, and repeat-last-week errors match.

## Future forecast

The future weeks are the next four Mondays after the last week in the data: 2026-03-02, 2026-03-09, 2026-03-16, and 2026-03-23. These are the forecasts currently saved. They remain March 2026 until the notebooks are run again on newer history. Every series in the processed data receives those four weeks.

For a long series, the model is trained on that series' full history and then forecasts one week at a time. Each prediction is appended and becomes an input for the next week. Later weeks therefore use earlier predictions. They do not use actual sales from weeks that have not happened.

The saved forecast values are rounded to two decimal places. The accuracy test uses the unrounded predictions.

Series that end before February 2026 still receive the March weeks. `Last Observed Week` records the last real week. A history is recent when that week is 2026-01-26 or later. An older history is stale. A stale series is still forecast from its own last observations.

The March models are fit on all available history. The models in the accuracy test stop at each cutoff. Those are two different fits.

## Accuracy test

The test is chronological. There is no random train/test split.

There are eight cutoffs, one week apart, from 2025-12-08 through 2026-01-26. From each cutoff the model forecasts four weeks ahead. After the last cutoff, those four weeks run through 2026-02-23.

A series is scored at a cutoff only when all of these are true:

- the cutoff week was observed for that series
- at least 20 stored weeks exist through that cutoff
- the next four calendar weeks were also observed for that series

Training uses weeks up to and including the cutoff. Demand after the cutoff is used only to compute the error.

The baseline repeats the cutoff week's demand for all four weeks.

This is the same eligible set as notebook 4's rolling-origin test:

| Dataset | Series-cutoff pairs | Scored weeks |
| --- | --- | --- |
| Levi's SKU | 224 | 896 |
| Souled Store SKU | 1,461 | 5,844 |
| Levi's category | 15 | 60 |
| Souled Store category | 528 | 2,112 |

Notebook 5 recomputed the repeat-last-week error on this set and matched the saved file at every horizon before comparing XGBoost with it.

`outputs/ml_model_evaluation.csv` is a different test. There, each held-out week still uses the real previous week, and one shared model sees a category code for location and item. Those one-step numbers are not the comparison in notebook 5.

## Metrics

MAE is the average absolute error. A few very large weeks can make it large. Median absolute error is the error of a typical scored week. Both are reported by dataset and by horizon (1, 2, 3, and 4 weeks ahead, plus all four weeks together).

The comparison also counts, week by week, whether XGBoost or repeat-last-week is closer. That count is only between those two methods. Random Forest is compared through its saved MAE and median absolute error, because its week-by-week predictions were not stored.

## Assumptions

- Weekly demand at a location and item can be forecast from that series' own earlier weeks.
- Monday is the shared week label after the one-day category shift.
- A gap in a category series stays a gap.
- Twenty observed weeks is enough history to train the lag model. Fewer weeks use the recent average.
- Repeating the cutoff week for four weeks is the baseline carried forward from notebook 4.
- Large historical weeks stay in the training data. None are deleted or capped.
- The XGBoost settings above are a fixed, simple choice. They are not a claim that another learning rate or tree count would score the same way.
