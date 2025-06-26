import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

model = LinearRegression()
def main():
    # prepare data
    print("load data")
    df = pd.read_csv('data.csv', header=None)
    df.columns = ['input1', 'input2', 'input3', 'result']
    df.head()

    # X = df.iloc[:, :3]
    # y = df.iloc[: 3]
    X = df[['input1', 'input2', 'input3']]  # shape: (500, 3)
    y = df['result']


    print("trainning model")
    # training
    model.fit(X, y)

    print("Model Coefficients:", model.coef_)
    print("Model Intercept:", model.intercept_)
    print(f"\nFormula: result = {model.coef_[0]:.2f} * input1 + {model.coef_[1]:.2f} * input2 + {model.coef_[2]:.2f} * input3 + {model.intercept_:.2f}")

    # test
    print("result = ", predict(0.5, 0.5, 0.2))
    test_input = [[0.5, 0.5, 0.2]]
    predicted = model.predict(test_input)[0]
    print(f"\nTest input: {test_input}")
    print(f"Predicted result: {predicted:.4f}")


    # check accurate predictions
    y_pred = model.predict(X)
    # Evaluate
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    rmse = mse ** 0.5
    r2 = r2_score(y, y_pred)

    # Show results
    print("Check accurate predictions")
    print(f"MAE  (Mean Absolute Error): {mae:.4f}") # 0 → better
    print(f"MSE  (Mean Squared Error) : {mse:.4f}")
    print(f"RMSE (Root Mean Squared)  : {rmse:.4f}") # 0 → better
    print(f"R² Score (R-squared)      : {r2:.4f}") #  to 1 → better

    plt.scatter(y, y_pred, alpha=0.5)
    plt.xlabel("Actual Result")
    plt.ylabel("Predicted Result")
    plt.title("Actual vs Predicted")
    plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--')  # Perfect prediction line
    plt.show()


def predict(input1, input2, input3):
    print("predict")
    return model.predict([[input1, input2, input3]])[0]


main()
