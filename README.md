# Exploratory Data Distribution Analysis

A reusable Python project for performing an initial statistical and visual assessment of numerical datasets. The notebook helps identify missing values, unusual distributions, outliers, skewness, and relationships between variables before building machine-learning models.

## Project objective

The goal is to provide a clear exploratory workflow that can be applied to a CSV dataset with minimal changes. It is designed as an educational data-analysis project and as a starting template for future analytics work.

## Analysis included

- Dataset shape, data types, and missing-value checks
- Descriptive statistics for numerical and categorical columns
- Histograms for numerical distributions
- Box plots and IQR-based outlier detection
- Correlation analysis using a heatmap
- Mean, median, standard deviation, skewness, and kurtosis summaries
- Basic data-quality validation

## Technologies used

- Python
- pandas
- NumPy
- matplotlib
- seaborn
- SciPy
- Jupyter Notebook

## Repository structure

```text
data/
  README.md
notebooks/
  exploratory_data_distribution_analysis.ipynb
README.md
requirements.txt
LICENSE
.gitignore
```

## How to run

1. Clone or download this repository.
2. Place a permitted CSV file in the `data` folder and name it `dataset.csv`.
3. Install the dependencies:

```bash
pip install -r requirements.txt
```

4. Start Jupyter Notebook:

```bash
jupyter notebook notebooks/exploratory_data_distribution_analysis.ipynb
```

5. Run the notebook cells from top to bottom.

## Expected outputs

The notebook produces summary tables, distribution plots, box plots, an outlier summary, a correlation matrix, and distribution diagnostics. The exact findings depend on the dataset supplied by the user.

## Limitations

- The repository does not include a public dataset yet.
- The workflow focuses mainly on numerical variables.
- Outlier detection uses the IQR rule and may need adjustment for domain-specific data.
- The notebook is intended for exploratory analysis rather than automated production reporting.

## Future improvements

- Add an example public dataset
- Add categorical-variable visualizations
- Add automated data-quality reporting
- Export charts and findings to an HTML or PDF report
- Build a small Streamlit interface

## Author

**Muhammad Kamil Shah**  
BS Data Science

## License

This project is licensed under the MIT License.
