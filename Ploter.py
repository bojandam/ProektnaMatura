# import all the required files
import numpy as np
from matplotlib import pyplot as plt

# sklearn import
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def plot(Y, degs, colors, name: str):
    plt.figure(figsize=(13, 5))
    X = np.array(range(len(Y))).reshape(-1, 1)
    y = Y[:]
    plt.scatter(X, y, label="training points", color=colors["plot"], s=1)
    models = []
    for degree in degs:
        model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=0.1e-3))
        model.fit(X, y)
        models.append(model)
        y_pred = model.predict(X)
        # if degree == 1:
        #     slope = (y_pred[-1] - y_pred[0]) / (len(Y))
        #     slope = np.arctan(slope)
        #     slope = np.degrees(slope)
        #     print("Slope: ", slope)
        #     print(
        #         y_pred[0],
        #         y_pred[-1],
        #         len(Y),
        #         y_pred[-1] - y_pred[0],
        #         (y_pred[-1] - y_pred[0]) / (len(Y)),
        #         np.arctan((y_pred[-1] - y_pred[0]) / (len(Y))),
        #         np.degrees(np.arctan((y_pred[-1] - y_pred[0]) / (len(Y)))),
        #     )
        #     plt.plot([], [], label="Slope: " + str(np.round(slope, 6)) + "°")
        plt.plot(X, y_pred, linewidth=2, label="deg %d" % degree, color=colors[degree])

    plt.legend(loc="upper left")
    plt.title(name)
    plt.savefig(name + ".png", dpi=600)

    plt.show()
