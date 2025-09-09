This project is a Streamlit-based web application for visualizing historical stock prices and comparing model-predicted closing prices against actuals. The core of the app is an already trained LSTM model stored in `Stock_prediction_model.h5`, which is loaded at runtime to generate predictions. The UI is built with Streamlit (`import streamlit as slt`) and provides a single text input for the user to enter a stock ticker (default: AAPL). Once a ticker is provided, the app uses `yfinance` to download daily historical data between 2010-01-01 and 2022-12-31.

After data retrieval, the app displays a descriptive summary (`df.describe()`) and renders multiple charts using Matplotlib: a simple “Closing Price vs Time” chart, a 100-day moving average overlay, and a combined 100-day and 200-day moving average overlay. These plots help users quickly understand long-term trends and momentum. The smoothing via rolling averages illustrates typical behavior around trend-following techniques, providing context before model predictions.

For prediction, the dataset is split chronologically into training (first 70% of rows) and test (remaining 30%) portions, focusing on the `Close` column. The training segment is scaled to the [0, 1] range using `MinMaxScaler`. The app constructs supervised learning sequences with a sliding window of 100 time steps: for each index, the previous 100 scaled closing prices are the input (`x_train`), and the current price is the target (`y_train`). The pre-trained LSTM model is then loaded from `Stock_prediction_model.h5`.

On the test side, the app concatenates the last 100 days of the training data with the test data to provide initial context, scales this combined frame, and constructs `x_test` and `y_test` in the same 100-step rolling fashion. The LSTM generates predictions for each test window. Because predictions and targets are in scaled units, the app rescales both back to the original price space using the inverse of the scaler’s learned factor. Finally, it plots “Predictions vs Original” to visually compare how well the model tracks the true closing prices over time.

From a runtime perspective, the app is launched with Streamlit (e.g., `streamlit run app.py`). We ensured compatibility on your Python 3.8 environment by downgrading `multitasking` to 0.0.11 to avoid PEP 585 typing that broke on 3.8. We also installed Streamlit and its dependencies. Note that installing Streamlit upgraded `typing-extensions`, which may conflict with `tensorflow-intel 2.13.0`. If you encounter model-loading errors or runtime issues related to typing versions, either pin `typing-extensions<4.6` or upgrade TensorFlow to a version compatible with the current `typing-extensions`.

Overall, the app provides an accessible interface for end users to:
- Fetch historical price data by ticker.
- Explore summary statistics and key trend plots (MAs).
- View side-by-side comparisons of actual vs predicted closing prices.

The heavy lifting—sequence preparation, scaling, and LSTM inference—is performed automatically behind the scenes, making it easy to experiment with different tickers and understand model behavior over a fixed historical window.
