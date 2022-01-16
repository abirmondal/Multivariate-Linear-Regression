import datagen
import modelgen as mgen
import modelplot as mplt
import pandas
import numpy as np


def main():
    nD = 3
    xDataLowerLimit = 10
    xDataUpperLimit = 15
    mDataLowerLimit = 5
    mDataUpperLimit = 8
    epoch = 200
    datagen.gen_data(nD, xDataLowerLimit, xDataUpperLimit,
                     mDataLowerLimit, mDataUpperLimit, epoch)
    pr = pandas.read_csv("data.csv")
    print("\nNumber of Data Points : ", epoch)
    print("Training Set : ", epoch - 15)
    print("Testing Set : ", 15)
    print("\n")

    mSet = mgen.traindata(
        pr.values[:epoch - 15, 1:], pr.values[:epoch - 15, 0], 0.0001)
    c = mSet[1]
    epochs = mSet[2]
    losses = mSet[3]
    mSet = mSet[0]

    nTrain = epoch - 15
    xSetTest = pr.values[nTrain + 1:, 1:]
    ySetTest = pr.values[nTrain + 1:, 0]
    if xSetTest.shape[1] > 1:
        xSetTest = mgen.normalize(xSetTest)
    yPredTest = np.zeros((ySetTest.shape))
    for i in range(len(xSetTest)):
        yPredTest[i] = c
        for j in range(xSetTest.shape[1]):
            yPredTest[i] = yPredTest[i] + (xSetTest[i][j] * mSet[j])
        # print(ySetTest[i], yPredTest[i])
    header_data = {"Y (Actual)": ySetTest, "Y (Predicted)": yPredTest}
    df = pandas.DataFrame(header_data)
    print("\n")
    print(df.to_string(index=False))

    mplt.showPlot(epochs, losses, pr.values, mSet, c)


if __name__ == '__main__':
    main()
