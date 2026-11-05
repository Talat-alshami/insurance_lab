# 🎲 Project 03: Probability & Uncertainty Lab

## 📌 Overview
In this project, we moved beyond descriptive statistics to quantify uncertainty and predict risk using the `insurance_clean.csv` dataset (1,337 records). The objective was to answer critical business questions for an insurance company regarding the likelihood of high medical costs, using both empirical data and theoretical probability distributions.

---

## 📊 Key Findings & Probabilities

### 1. Baseline Probability (Marginal)
*   **Probability of a New Insured being a Smoker:** `0.2049` (20.49%)
    *   *Insight:* Approximately 1 in 5 clients are smokers.
*   **Overall Probability of Charges > 20,000:** `0.2042` (20.42%)
    *   *Method:* Empirical calculation (Direct counting).

### 2. The Failure of Normal Approximation
*   **Normal Distribution Approximation for P(Charges > 20,000):** `0.2895` (28.95%)
    *   *Insight:* The normal approximation significantly **overestimated** the probability. Because `charges` is heavily right-skewed (due to extreme outliers like major surgeries), the mean (13,279) and standard deviation (12,110) are inflated. This creates a flattened bell curve that does not represent the true concentration of data, making the Normal distribution an invalid tool here.

### 3. Conditional Probability (Direct Filtering)
*   **P(Charges > 20,000 | Smoker):** `0.7737` (77.37%)
    *   *Insight:* If a person smokes, there is a **77% chance** their medical costs will exceed 20,000. Smoking is a massive risk multiplier.
*   **P(Charges > 20,000 | Non-Smoker):** `0.0574` (5.74%)
    *   *Insight:* The probability drops drastically for non-smokers.

### 4. Bayes' Theorem (Inverse Probability)
*   **P(Smoker | Charges > 25,000):** `0.8358` (83.58%)
    *   *Method:* Calculated using Bayes' Theorem and verified via direct filtering.
    *   *Insight:* If a claim exceeds 25,000, there is an **83.58% probability** that the client is a smoker. This is a crucial "Evidence-Based" insight for the underwriting department to flag high-risk claims.

---

## 🛠️ Mathematical Concepts Applied
1.  **Empirical Probability:** Direct counting from the dataset, free of theoretical assumptions.
2.  **Conditional Probability:** Calculating the likelihood of an event given prior knowledge ($P(A|B)$).
3.  **Bayes' Theorem:** Updating the probability of a hypothesis as more evidence becomes available ($P(\text{Smoker}|\text{High Cost})$).
4.  **Z-Score & Normal Distribution:** Applied to demonstrate mathematically why parametric distributions fail when data is heavily skewed by outliers.

---

## 💻 Engineering & Validation
*   **Cross-Validation:** Every probability calculated using a formula (like Bayes) was independently verified using direct DataFrame filtering to ensure mathematical and programmatic accuracy.
*   **Floating-Point Precision:** Handled minor decimal differences naturally occurring in Python floats.

---

## 🧠 Mastery Log
*   [x] **Distinguishing Probability Levels:** Mastered the difference between individual probability, joint probability, and conditional probability.
*   [x] **Tool Selection:** Correctly identified when to use empirical counting vs. theoretical distributions.
*   [x] **Critical Thinking:** Recognized that complex math (Normal/Bayes) is not always the right tool; the right tool depends entirely on the data's nature and the question's direction.
*   [x] **Business Interpretation:** Successfully translated statistical outputs into actionable business decisions (e.g., risk flagging for costs > 25k).

**Status:** ✅ **Mastered (100%)**

---

## 🔜 Next Steps
Moving to **Project 04: Relationships & Dependence**. We will investigate the linear and non-linear relationships between variables (Age, BMI, Charges), explore Covariance vs. Correlation, and identify potential Confounding Variables.