# sap2012
SAP2012 energy calculation method in Python.

## Introduction

SAP2012 is the Standard Assessment Procedure 2012, the UK Government's energy calculation method for the building regulation compliance for new dwellings. 

SAP2012 is developed and published by the Building Research Establishment: https://www.bregroup.com/sap/standard-assessment-procedure-sap-2012/.

This Python package contains the calculation methods and data in the SAP2012 methodology. It allows the user to specify the inputs needed for a SAP calculation and then to run a SAP calculation based on these inputs.

## Approach

The package is designed to represent the SAP calculation method as simply as possible, to allow for flexibility and customisation based on the underlying equations and data of the method. 

Each section of the SAP2012 calculation method is a separate Python function which takes the input data as a series of arguments and returns the calculation results. For example, the method for calculating ventilation rates is given in the [ventilation_rates.py](./sap2012/calcs/ventilation_rates.py) module.

A complete SAP calculation is run using the Sap2012 class.

## Quick Example

### Creating a Sap2012 instance

```python
>>> from sap2012 import Sap2012
>>> s=Sap2012()
```

### Reading in model inputs from a csv file

```python
>>> s.read_input_csv('my_input_file.csv')
>>> print(len(s.inputs))
197
>>> print(s.inputs['external_wall_u_value'])
1.5
```

See [here](./demo/input_csv_file.csv) for an example of an input csv file. The inputs could also be specified by updating the *inputs* dictionary values.

### Run a SAP calculation

```python
>>> s.run()
>>> print(len(s.outputs))
192
```

The complete set of calculation outputs is stored in the *outputs* dictionary.

### View calculation results

```python
>>> print(s.outputs['total_energy_used'])
16499.45199251753	
```

This is the total energy used by the house in kWh. 

## Issues & feature requests?

Please raise them on the [GitHub Issues page](https://github.com/building-energy/sap2012/issues).

## Contributions

All contributions welcome. Please send your [pull requests](https://github.com/building-energy/sap2012/pulls).

## Contacts

https://www.lboro.ac.uk/departments/abce/staff/steven-firth/









