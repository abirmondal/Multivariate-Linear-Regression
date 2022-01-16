# Multivariate-Linear-Regression

This is a code done from **scratch**.

## Features

### Generates n-dimensional data set

It generates a n-dimensional data set and then stores in a _.csv_ file named **data.csv**.<br>
To use this feature use the **gen_data** module _datagen_ library. This module takes in _6_ parameters,

- **dimesion**: Value of the dimension for the data set that needs to be genrated like 2, 3, 4, ... .
- **x_lower_range**: The lower range value of _x_ for data generation.
- **x_higher_range**: The higher/upper range value of _x_ for data generation.
- **m_lower_range**: The lower range value of _m_ for data generation.
- **x_higher_range**: The higher range value of _m_ for data generation.
- **epoch**: Number of data points.
