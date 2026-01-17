# import all the required files
import numpy as np
from matplotlib import pyplot as plt

# sklearn import
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline


def oldPlot(plt, Y, degs, colors, linesyles, name: str = ""):
    if name != "":
        name += " "
    X = np.array(range(len(Y))).reshape(-1, 1)
    y = Y[:]
    plt.scatter(
        X,
        y,
        # label=name + "training points",
        color=colors["plot"],
        s=1,
    )
    models = []
    for degree in degs:
        model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=0.1e-3))
        model.fit(X, y)
        models.append(model)
        y_pred = model.predict(X)

        """# if degree == 1:
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
        #     plt.plot([], [], label="Slope: " + str(np.round(slope, 6)) + "°") """
        plt.plot(
            X,
            y_pred,
            linewidth=2,
            label=name if degree != 1 else None,
            linestyle=linesyles[degree],
            color=colors[degree],
        )

    plt.legend(
        loc="lower right",
        # bbox_to_anchor=(1.05, 1)
    )


def plot(Y, degs, colors, linestyles, name: str):
    plt.figure(figsize=(13, 5))
    oldPlot(plt, Y, degs, colors, linestyles)
    plt.title(name)
    plt.show()
    plt.savefig(name + ".png", dpi=600)


def plot_two(
    ListOfInput, name: str, xlabel: str = "", ylable: str = "", figsize=(13, 5)
):
    """
    ListOfInput: Consists of tupples of:\n
    \tY: List of values\n
    \tdegs: List of polinomial degrees to aproximate\n
    \tcolors: Dictionary with color info per polyinomial\n
    name: Name of graph\n
    name: str\n
    """
    plt.figure(figsize=figsize)

    for Y, degs, colors, linestyles, which in ListOfInput:
        oldPlot(plt, Y, degs, colors, linestyles, which)
    plt.title(name)
    plt.xlabel(xlabel)
    plt.ylabel(ylable)
    plt.show()
    plt.savefig(name + ".png", dpi=600)
