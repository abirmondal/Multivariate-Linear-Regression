import random
import pandas as pd
import numpy as np


def gen_data(dimension, x_lower_range, x_higher_range, m_lower_range, m_higher_range, epoch):
    data = []
    slopes = []  # incase if needes
    # y = c + m1x1 + m2x2 + .....
    if dimension == 2:
        x = []
        for i in range(0, epoch):
            xTemp = np.random.uniform(
                x_lower_range, x_higher_range, dimension - 1)
            xTemp = np.sort(xTemp, axis=0)
            x.append(xTemp)
        x = np.array(x)
        x = np.sort(x, axis=0)
        x = x.reshape((epoch,))
        print(x)

        y = []
        m = np.random.randint(m_lower_range, m_higher_range,
                              size=dimension, dtype=int)
        for i in range(0, epoch):
            yTemp = np.sum(x[i] * m) + random.randint(-5, 5)
            y.append(yTemp)
        y = np.array(y)
        print(y)

        header_data = {"Y": y, "X0": x}
        df = pd.DataFrame(header_data)
        df.to_csv('data.csv', header=True, index=False)

    else:
        for i in range(epoch):
            return_li = []
            x = []
            m = []  # m0 is the constant
            for i in range(dimension - 1):
                x_item = random.uniform(x_lower_range, x_higher_range)
                x.append(x_item)

            for i in range(dimension):
                m_item = random.uniform(m_lower_range, m_higher_range)
                m.append(m_item)

            y = m[0]
            for i in range(0, len(x)-1):
                y += m[i+1] * x[i]
            return_li.append(y)

            for i in x:
                return_li.append(i)
            data.append(return_li)
            slopes.append(m)

        # adding heading to the csv
        header_data = {}
        Y = []
        for i in data:
            Y.append(i[0])
        header_data.update({'Y': Y})

        for i in range(1, len(data[0])):
            X = []
            for j in data:
                X.append(j[i])
            header_data.update({f"X{i-1}": X})

        # Y = []
        # for i in data:
        #     Y.append(i[0])
        # header_data.update({'Y': Y})

        # writing data to csv file
        df = pd.DataFrame(header_data)
        df.to_csv('data.csv', header=True, index=False)
