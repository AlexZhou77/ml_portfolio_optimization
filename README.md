# ⭐ ASTRA: An Automated Daily Trading Pipeline

### **Overview**

In this project, we build a prototype of **ASTRA** (Automated Sentiment-driven Trading and Risk Allocation). It is an **end-to-end automated trading system** that combines machine learning models with Markowitz portfolio theory. Each day after the market closes, our system retrieves market data(OHLCV) and company-related market news. We then generate technical indicators from the market data, compute sentiment scores from the news, and use these features as inputs to pre-trained ML model to predict next-day price movements. In addition, we compute the optimal portfolio weights using Markowitz's theory. We then record the predicted directions and weights as JSON files, which are sent to our TradingView front-end for visualization and performance monitoring. The workflow is illustrated in the diagram below:

<img width="8926" height="6878" alt="flow" src="https://github.com/user-attachments/assets/db7c0f8f-896c-4cac-aa7f-173f9a54c2da" />


## Price Movement Prediction

We selected ten popular stocks for our portfolio: NVDA, GOOG, AAPL, AMZN, MSFT, SPOT, TSLA, JPM, GS, and LMT. These tickers were chosen for their extensive news coverage, which helps improve the reliability of sentiment-based features.

Using data from 2021-10-15 to 2025-10-16, we trained three machine learning models: **K-Nearest Neighbors (KNN), Logistic Regression, and Support Vector Machines (SVM)**. The Logistic Regression model achieved the best performance:

<img width="794" height="480" alt="Performance" src="https://github.com/user-attachments/assets/c2c11738-46d2-43f7-a84e-cd7b20d566d1" />

As we can see, for all stocks, the prediction accuracy is above 50% (better than a coin toss). Another baseline we use is the “always-up” baseline, since the selected stocks are strong market performers and tend to rise on most days. It turns out that for 9 out of 10 stocks, our model outperforms the always-up baseline, with notable improvements for NVDA (about 4%), AAPL (about 3%), and TSLA (about 10%). Moreover, for NVDA, TSLA, and JPM, the testing accuracy reaches nearly 60%. This suggests that following the model’s buy signals over time could lead to a positive expected return.

## Markowitz Portfolio Theory

Markowitz Portfolio Theory was introduced by Harry Markowitz in 1952. It is a mathematical framework for constructing an investment portfolio that balances risk and return. The key idea is that the risk of a portfolio is not just the weighted sum of individual asset risks but also depends on how the assets’ returns co-vary with each other. By combining assets with imperfectly correlated returns, investors can reduce overall portfolio volatility via diversification. 

We compute the optimal weights for our portfolio using Markowitz's theory. For each day, we use stock data from the past year (from this day last year to today) to compute the average return and volatility. We then use these statistics to compute the optimal portfolio weights that yield the highest Sharpe ratio. Here’s a plot of the efficiency frontier for our portfolio:

<img width="1176" height="807" alt="The efficiency frontier" src="https://github.com/user-attachments/assets/de069d86-0916-4c91-b86f-5e26a46b4819" />

The computed weights are stored in `weights.json`. 

## Monitoring the portfolio in TradingView

We send `directions.json` and `weights.json` to our TradingView account via a pre-configured webhook. On TradingView, we use PineScript to parse the data and visualize the portfolio returns over time. We also generate buy and sell signals based on the predicted directions. Over time, we can paper trade on TradingView using these signals to evaluate how the strategy performs in real time.
