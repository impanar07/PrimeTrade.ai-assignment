# 📊 Crypto Trader Behavior vs Market Sentiment Analysis

## Project Overview

This project investigates how cryptocurrency traders behave under different market sentiment conditions using the **Fear & Greed Index** and historical trading data.

The objective is to determine whether market sentiment influences trader profitability, risk-taking behavior, leverage usage, and trading frequency.

---

## Objectives

- Clean and preprocess trading and sentiment datasets
- Merge datasets using daily timestamps
- Analyze trader performance across different market sentiments
- Study changes in trader behavior
- Segment traders based on behavioral characteristics
- Build a simple predictive model
- Develop an interactive Streamlit dashboard

---

## Dataset

### 1. Historical Trading Data
Contains individual trade information including:

- Account
- Timestamp
- Side (BUY/SELL)
- Size USD
- Closed PnL
- Start Position

### 2. Fear & Greed Index

Contains daily market sentiment:

- Date
- Fear & Greed Value
- Sentiment Classification

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit

---

## Methodology

### Data Preprocessing

- Loaded both datasets
- Checked missing values and duplicates
- Converted timestamps to daily dates
- Merged trading data with Fear & Greed Index

### Feature Engineering

Created:

- Daily PnL
- Win Rate
- Average Trade Size
- Estimated Leverage
- Long/Short Ratio
- Trade Frequency
- Drawdown Proxy

### Exploratory Data Analysis

Compared trader performance across:

- Fear
- Extreme Fear
- Neutral
- Greed
- Extreme Greed

Analyzed:

- Average PnL
- Win Rate
- Trade Frequency
- Position Size
- Leverage Distribution
- Long vs Short Bias

### Trader Segmentation

Clustered traders into behavioral archetypes:

- Conservative Traders
- Aggressive High-Leverage Traders
- Consistent Profitable Traders

### Predictive Model

Random Forest Classifier

Target:

- Profitable Trade
- Non-profitable Trade

Features:

- Sentiment Score
- Leverage
- Position Size
- Trade Frequency
- Trade Side

---

## Results

The analysis demonstrates that market sentiment influences both trader behavior and profitability.

Key metrics analyzed:

- Daily PnL
- Win Rate
- Drawdown
- Position Size
- Leverage
- Trade Frequency

---

## Strategy Recommendations

### Strategy 1

Reduce leverage and position size during Fear and Extreme Fear periods to limit downside risk.

### Strategy 2

Increase exposure cautiously during Greed periods while maintaining predefined risk limits and stop-loss rules.

---

## Streamlit Dashboard

Run locally:

```bash
pip install -r requirements.txt

streamlit run app.py
```

---

## Repository Structure

```
Crypto-Trader-Sentiment-Analysis/
│
├── data/
├── notebooks/
├── images/
├── app.py
├── requirements.txt
└── README.md
```

---

## Future Improvements

- Time-series forecasting of trader profitability
- XGBoost model for prediction
- Advanced trader segmentation
- Real-time sentiment API integration

---

## Author

Bindu Prakash
