Quick Example
=============

Creating a Sap2012 instance
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   >>> from sap2012 import Sap2012
   >>> s=Sap2012()


Reading in model inputs from a csv file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   >>> s.read_input_csv('my_input_file.csv')
   >>> print(len(s.inputs))
   197
   >>> print(s.inputs['external_wall_u_value'])
   1.5

See `here <https://github.com/building-energy/sap2012/blob/master/demo/input_csv_file.csv>`_ for an example of an input csv file. 
The inputs could also be specified by updating the *inputs* dictionary values.

Run a SAP calculation
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
   
   >>> s.run()
   >>> print(len(s.outputs))
   192

The complete set of calculation outputs is stored in the *outputs* dictionary.

View calculation results
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python
   
   >>> print(s.outputs['total_energy_used'])
   16499.45199251753	

This is the total energy used by the house in kWh. 

