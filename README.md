# Multivariate-Linear-Regression

This is a code done from **scratch**.

## Features

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