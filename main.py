import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.linear_model import SGDRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Lasso, Ridge
from sklearn.metrics import mean_squared_error as mse
from sklearn.linear_model import LinearRegression

data = pd.read_csv("data/data.csv", index_col=0)
data_predict = pd.read_csv("data/predict.csv", index_col=0)

plt.scatter(data["carat"], data["price"])
plt.xlabel("Carat")
plt.ylabel("Price"); 


y = data['price']
X = data.drop(columns=['price'])

## get_dummies

X_dummies = pd.get_dummies(X, columns=["cut", "color", "clarity"])

# Training and test, Data split

X_train, X_test, y_train, y_test = train_test_split(X_dummies, y, random_state=42)


models = {
    "LinearRegression":LinearRegression(),
    "Poly_2":Pipeline([("poly_features",PolynomialFeatures(degree=2)),
                       ("linear_regression", LinearRegression())]),
    #"Poly_3":Pipeline([("poly_features",PolynomialFeatures(degree=3)),
    #                   ("linear_regression", LinearRegression())]),
    #"Poly_4":Pipeline([("poly_features",PolynomialFeatures(degree=4)),
    #                   ("linear_regression", LinearRegression())]),
    #"Lasso":Lasso(alpha=1),
    #"Ridge":Ridge(alpha=1),
    #"Support Vector Machine":SVR(),
    #"SGD":SGDRegressor(),
    "Random Forrest": RandomForestRegressor(),
    "Polynomial_dg_2_Lasso":Pipeline([('poly', PolynomialFeatures(degree=3)),
                                      ("lasso",Lasso(alpha=1))]),
}


results_train = {}
results_test = {}

for name,model in models.items():
    model.fit(X_train, y_train)
    results_train[name] = mse(y_train, model.predict(X_train))**.5
    results_test[name] = mse(y_test, model.predict(X_test))**.5
    print(name)


pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.DataFrame({
    "Train":results_train,
    "Test":results_test
})

print(results_train)
print(results_test)
