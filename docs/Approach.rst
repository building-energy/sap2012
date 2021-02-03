Approach
========

The package is designed to represent the SAP calculation method as simply as possible, to allow for flexibility and customisation based on the 
underlying equations and data of the method. 

Each section of the SAP2012 calculation method is a separate Python function which takes the input data as a series of arguments and returns the calculation results. 
For example, the method for calculating ventilation rates is given in the `ventilation_rates` function.

A complete SAP calculation is run using the Sap2012 class.






