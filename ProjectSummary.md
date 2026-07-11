# Project Summary

## Methodology

Two datasets were analyzed: historical cryptocurrency trading records and the Fear & Greed Index. After preprocessing, timestamps were converted to daily dates and merged. New analytical features such as daily PnL, win rate, leverage, drawdown proxy, trade frequency, and position size were engineered. Exploratory analysis compared trader performance across different market sentiment categories. Traders were further segmented using K-Means clustering, and a Random Forest classifier was developed to predict trade profitability.

---

## Key Insights

### 1. Market Sentiment Influences Profitability

Trader profitability varied across Fear and Greed market conditions. Greed periods generally produced stronger trading performance, while Fear periods exhibited larger downside risk.

### 2. Traders Become More Aggressive During Greed

Trade frequency, leverage, and average position sizes increased during Greed periods, indicating higher risk appetite under positive market sentiment.

### 3. High-Leverage Traders Experience Greater Volatility

Although high-leverage traders generated larger profits on average, they also experienced significantly larger drawdowns, highlighting the trade-off between return and risk.

---

## Strategy Recommendations

### Strategy 1

Reduce leverage and position sizes during Fear and Extreme Fear periods to minimize drawdowns and preserve capital.

### Strategy 2

Increase position sizes cautiously during Greed periods while maintaining strict stop-loss and leverage limits to capitalize on favorable market trends without excessive risk.

---

## Conclusion

This project demonstrates how integrating market sentiment with trading behavior provides valuable insights into trader performance and risk management. The combination of exploratory data analysis, clustering, predictive modeling, and an interactive Streamlit dashboard offers a practical framework for sentiment-driven trading analytics.
