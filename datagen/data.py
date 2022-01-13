import random


def gen_data(dimension, x_lower_range, x_higher_range, m_lower_range, m_higher_range):
    data = []
    slopes = []  # incase if needes
    # y = c + m1x1 + m2x2 + .....
    for i in range(10):
        return_li = []
        x = []
        m = []
        for i in range(dimension):
            x_item = random.uniform(x_lower_range, x_higher_range)
            x.append(x_item)

        for i in range(dimension - 1):
            m_item = random.uniform(m_lower_range, m_higher_range)
            m.append(m_item)

        y = x[0]
        for i in range(len(x)-1):
            y += m[i] * x[i+1]

        return_li.append(y)

        for i in x:
            return_li.append(i)

        data.append(return_li)
        slopes.append(m)

    return data
