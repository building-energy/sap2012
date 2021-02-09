Quick Example
=============

This example:

- Imports the `calculate_worksheet` function.
- Reads in the 'inputs' dictionary from a json file (available to view `here <https://github.com/building-energy/sap2012/blob/master/notebooks/docs/inputs.json>`_).
- Runs the `calculate_worksheet` function with the 'inputs' dictionary.
- Prints the results of the `SAP_rating` section of the SAP worksheet (the full result dictionary is available to view `here <https://github.com/building-energy/sap2012/blob/master/notebooks/docs/result.json>`_).

.. code-block:: python

   >>> from sap2012 import calculate_worksheet
   >>> import json
   >>> with open('inputs.json') as f:
   >>>     inputs=json.load(f)
   >>> result=calculate_worksheet(inputs)
   >>> print(result['SAP_rating'])
   {'energy_cost_factor': 1.7754795340546146, 'SAP_rating_value': 75.23206049993813}

The format required for the 'inputs' dictionary is given in the documentation of the `calculate_worksheet` function.

The return value of the `calculate_worksheet` function is a dictionary containing the model outputs. This is also described in the `calculate_worksheet` documentation.




