   # CAP 3764 — Final Project: US Cost-of-Living Tracker

   ## Topic
   Tracking U.S. cost-of-living pressure through monthly grocery and gas prices (2015–2026).

   ## Dataset
   - Source: Kaggle (built from U.S. Bureau of Labor Statistics Average Price Data)
   - ~8,869 rows, monthly observations, 74 items across 12 categories (groceries + gasoline)
   - Variables: date, year, month, item, unit, category, price, series_id

   ## Problem
   Regression problem: predicting item price based on item type and date.

   ## Setup
   1. Clone this repo
   2. Create the environment: `conda env create -f environment.yml`
   3. Activate it: `conda activate team3_grocery_gas`
   4. Launch JupyterLab and select the environment's kernel

   ## Folder structure
   - `src/` — data collection module
   - `data_collection.ipynb` — loads and cleans the dataset
   - `us_average_prices_monthly.csv` — raw dataset
   - `environment.yml` — conda environment spec
