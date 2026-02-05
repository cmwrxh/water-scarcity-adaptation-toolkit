import numpy as np
from sklearn.linear_model import LinearRegression

def simple_rainfall_forecast(historical_mm=[600, 550, 480, 520], future_months=12):
    X = np.arange(len(historical_mm)).reshape(-1, 1)
    y = np.array(historical_mm)
    model = LinearRegression().fit(X, y)
    future_X = np.arange(len(historical_mm), len(historical_mm) + future_months).reshape(-1, 1)
    preds = model.predict(future_X)
    return preds

if __name__ == "__main__":
    print("Forecasted rainfall (mm):", simple_rainfall_forecast())
