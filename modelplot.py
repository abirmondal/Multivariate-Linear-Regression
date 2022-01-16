import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def showPlot(epochs, losses, dataSet, mSet, c):
    n = mSet.size + 1
    if n == 2:
        plt.figure("Multivariate Plot", figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.title("Epochs VS Losses")
        plt.plot(epochs, losses)
        plt.xlabel('Epochs')
        plt.ylabel('Losses')

        plt.subplot(1, 2, 2)
        plt.title("Linear Regression Plot")
        plt.scatter(dataSet[:, 1], dataSet[:, 0])
        yPred = np.zeros((dataSet[:, 0].shape))
        xGiven = dataSet[:, 1]
        for i in range(0, xGiven.size):
            yPred[i] = c
            yPred[i] = yPred[i] + (xGiven[i] * mSet[0])
        plt.plot(dataSet[:, 1], yPred, c="r")
        plt.xlabel('X')
        plt.ylabel('Y')
    elif n == 3:
        fig = plt.figure("Multivariate Plot", figsize=(12, 6))
        plt.subplot(1, 2, 1)
        plt.title("Epochs VS Losses")
        plt.plot(epochs, losses)
        plt.xlabel('Epochs')
        plt.ylabel('Losses')

        ax = fig.add_subplot(1, 2, 2, projection='3d')
        plt.title("Linear Regression Plot")
        data = pd.read_csv("data.csv")
        data = data.values
        ax.scatter(data[:, 1], data[:, 2],
                   data[:, 0], c="blue")
        yPred = np.zeros((data[:, 0].shape[0]))
        xGiven = dataSet[:, 1:]
        for i in range(0, yPred.size):
            yPred[i] = c
            for j in range(0, xGiven.shape[1]):
                yPred[i] = yPred[i] + (xGiven[i][j] * mSet[j])
        ax.plot3D(data[:, 1], data[:, 2], yPred, c="green")

    elif n > 3:
        plt.figure("Multivariate Plot", figsize=(6, 6))
        plt.title("Epochs VS Losses")
        plt.plot(epochs, losses)
        plt.xlabel('Epochs')
        plt.ylabel('Losses')
    plt.show()
