import random
import numpy as np


def gen_data(dimension, x_lower_range, x_higher_range, m_lower_range, m_higher_range):
    data = []
    slopes = []  # incase if needes
    # y = c + m1x1 + m2x2 + .....
    for i in range(10):
        return_li = []
        x = []
        m = []
        for i in range(dimension - 1):
            x_item = random.uniform(x_lower_range, x_higher_range)
            x.append(x_item)

        for i in range(dimension - 2):
            m_item = random.uniform(m_lower_range, m_higher_range)
            m.append(m_item)

        y = 0
        for i in range(len(x)-1):
            if i == 0:
                y += x[i]
            else:
                y += m[i] * x[i]
        return_li.append(y)
        for i in x:
            return_li.append(i)
        data.append(return_li)
        slopes.append(m)
    for i, j in zip(data, slopes):
        print("data: ", i, "slopes: ", j)

    return data


if __name__ == "main":
    test = gen_data(2, 10, 20, 2, 4)
    print("The final data generated is: ")
    print(test)
