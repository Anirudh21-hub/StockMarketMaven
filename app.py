import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf

# from keras.models import load_model
import streamlit as slt
from keras.models import load_model

start = "2010-01-01"
end = "2022-12-31"

slt.title("STOCK TREND PREDICTION")

user_input = slt.text_input("ENTER STOCK TICKER", "AAPL")


df = yf.download(user_input, start, end)
# df.head()

slt.subheader("DATA FROM 2010 TO 2022")
slt.write(df.describe())


slt.subheader("CLOSING PRICE VS TIME CHART")
fig = plt.figure(figsize=(12, 6))
plt.plot(df.Close)
plt.xlabel("TIME(YRS)")
plt.ylabel("CLOSING PRICE")
slt.pyplot(fig)


slt.subheader("CLOSING PRICE VS TIME CHART WITH 100MPA")
ma100 = df.Close.rolling(100).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(ma100)
plt.plot(df.Close)
plt.xlabel("TIME(YRS)")
plt.ylabel("CLOSING PRICE")
slt.pyplot(fig)


slt.subheader("CLOSING PRICE VS TIME CHART WITH 200MPA")
ma200 = df.Close.rolling(200).mean()
fig = plt.figure(figsize=(12, 6))
plt.plot(ma100, "r")
plt.plot(ma200, "g")
plt.plot(df.Close)
plt.xlabel("TIME(YRS)")
plt.ylabel("CLOSING PRICE")
slt.pyplot(fig)


data_train = pd.DataFrame(df["Close"][0 : int(len(df) * 0.70)])
data_test = pd.DataFrame(df["Close"][int(len(df) * 0.70) : int(len(df))])
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler(feature_range=(0, 1))

data_train_array = scaler.fit_transform(data_train)

x_train = []
y_train = []
for i in range(100, data_train_array.shape[0]):
    x_train.append(data_train_array[i - 100 : i])
    y_train.append(data_train_array[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
model = load_model("Stock_prediction_model.h5")


past_100_days = data_train.tail(100).copy()

final_df = pd.concat([past_100_days, data_test], ignore_index=True)

input_data = scaler.fit_transform(final_df)
x_test = []
y_test = []
for i in range(100, input_data.shape[0]):
    x_test.append(input_data[i - 100 : i])
    y_test.append(input_data[i, 0])
x_test, y_test = np.array(x_test), np.array(y_test)

y_pred = model.predict(x_test)

scaler = scaler.scale_
scaler_factor = 1 / scaler[0]
y_pred = y_pred * scaler_factor
y_test = y_test * scaler_factor


slt.subheader("PREDICTIONS VS ORIGINAL")
fig2 = plt.figure(figsize=(12, 6))
plt.plot(y_test, "b", label="ORIGINAL PRICE")
plt.plot(y_pred, "r", label="PREDICTED PRICE")
plt.xlabel("TIME")
plt.ylabel("PRICE")
# plt.ylim(0, 400)
plt.legend()
slt.pyplot(fig2)
