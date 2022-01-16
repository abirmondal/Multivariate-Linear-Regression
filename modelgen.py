from math import sqrt
import numpy as np

def normalize(datas):
    mu = np.mean(datas, axis=0)
    sigma = np.std(datas, axis=0, ddof=1)
    for i in range(len(datas)):
        datas[i] = (datas[i] - mu) / sigma
    return datas


def traindata(xSet, ySet, lr):
    nSlope = xSet.shape[1]
    nTrain = xSet.shape[0]

    if nSlope > 1:
        xSet = normalize(xSet)
    m = np.zeros(nSlope)
    c = 0

    e = 0
    epochs = []
    losses = []
    lossDiff = 1
    prevLoss = 100
    limitLossDiff = 0.1**5

    while(abs(lossDiff) > limitLossDiff):
        loadStrSize = 6  # This print style is for 'For' loop
        if lossDiff < 1:
            print("Data Proccessing" + "."*(e % loadStrSize) + " "*(loadStrSize - (e % loadStrSize)),
                " ( %.2f%% )" % ((1 - lossDiff)/(1 - limitLossDiff)*100), end='\r')
        summ = np.zeros(nSlope)
        sumc = 0
        loss = 0

        for k in range(0, nTrain):
            ypred = c
            for i in range(0, nSlope):
                ypred = ypred + (xSet[k][i]*m[i])
            sumc = sumc + (ySet[k] - ypred)
            for i in range(0, nSlope):
                summ[i] = summ[i] + xSet[k][i]*(ySet[k] - ypred)
            loss = loss + (ySet[k] - ypred)*(ySet[k] - ypred)

        Dc = -1*sumc/nTrain
        Dm = np.zeros(nSlope)
        loss = loss/nTrain
        loss = sqrt(loss)
        for i in range(0, nSlope):
            Dm[i] = (-1*summ[i]/nTrain)

        for i in range(0, nSlope):
            m[i] = m[i] - lr*Dm[i]
        c = c - lr*Dc

        epochs.append(e+1)
        losses.append(loss)

        lossDiff = prevLoss - loss
        prevLoss = loss
        e = e + 1
    
    return [m, c, epochs, losses]