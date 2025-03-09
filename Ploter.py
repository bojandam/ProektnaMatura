# import all the required files
import numpy as np
from matplotlib import pyplot as plt

# sklearn import
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def plot(Y, degs, colors, name: str):
    plt.figure(figsize=(20, 3))
    X = np.array(range(len(Y))).reshape(-1, 1)
    y = Y[:]
    plt.plot(X, y, label="training points", color=colors["plot"])
    models = []
    for degree in degs:
        model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=0.1e-3))
        model.fit(X, y)
        models.append(model)
        y_pred = model.predict(X)
        plt.plot(
            X, y_pred, linewidth=2, label="degree %d" % degree, color=colors[degree]
        )

    plt.legend(loc="upper left")
    plt.title(name)
    plt.savefig(name + ".png", dpi=600)

    plt.show()
