Approach
========

The package is designed to represent the SAP calculation method as simply as possible, to allow for flexibility and customisation. 

Each section of the SAP2012 calculation method is implemented as a separate Python function which takes the input data as a series of arguments and returns the calculation results. 
For example, the method for calculating ventilation rates (SAP worksheet Section 2) is given by the `ventilation_rates` function.

A complete SAP calculation is run using the `calculate_worksheet` function.

.. note::

   This is a partial implementation of the Standard Assessment Procedure for the most common use case. 
   The complete procedure includes many additional calculation options in Appendices and many additional reference tables.
   
.. note::

   It is recommended that users carry out their own validation of the calculation results given by this Python package.
   The package has been validated for a common use case. 
   But there are many edge cases possible given the complex nature of the SAP procedure and all possible edge cases have not been checked.




