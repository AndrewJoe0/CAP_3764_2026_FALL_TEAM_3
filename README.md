
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
   - `data/` — raw dataset (`us_average_prices_monthly.csv`)
   - `notebooks/` — analysis notebooks (`data_collection.ipynb`)
   - `src/` — reusable Python code (data loading, cleaning, evaluation)
   - `reports/` — executive summary report
   - `environment.yml` — conda environment spec
