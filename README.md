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

### Plots the models
After the model is trained *2D* and *3D* trained data models are plotted. Also **Epoch VS Loss** curve is plotted in the same window.<br>
To use this feature use the **showPlot** module *modelplot* library. This module takes in *5* parameters,
* **epochs**: Epoch array for the *Epoch vs Loss* curve.
* **lossed**: Loss array for the *Epoch vs Loss* curve.
* **dataSet**: The whole data set that will be used to plot the model.
* **mSet**: The list of slopes of the trained model.
* **c**: The constant of the trained model.

### Print tabular data after training
A comparission of *y* value of original dataset and *y* predicted value for particular data points. For this the **test set** will be used to find the *y* predicted.