# Change Log - Project 02: Data Quality & Preparation

## Date: [2026/11/3]

## Source
- Input: `data/raw/insurance.csv` (1338 rows, 7 columns)
- Output: `data/processed/insurance_clean.csv` (1337 rows, 7 columns)

## Changes Applied
1. **Duplicates:** Removed 1 exact duplicate row. Used `drop_duplicates()` keeping the first occurrence.
2. **Missing Values:** None found (0 across all columns). No imputation needed.
3. **Outliers (charges):** Retained all 139 outliers. Rationale: In health insurance, high charges represent severe medical cases (not data entry errors). These are critical for future ML models.
4. **Data Types:** Categorical columns (`sex`, `smoker`, `region`) were left as strings (`object`). Rationale: To preserve interpretability for EDA and relationships analysis. Encoding (e.g., One-Hot) will be handled dynamically in the ML pipeline (Project 7).
5. **Data Validation:** Implemented `pytest` to validate no duplicates, no missing values, valid ranges (age >= 18, bmi > 0, charges > 0), and correct row count (1337).

## Status
- 4/4 `pytest` tests passed. Data is clean and ready for Project 3 (Probability Lab).