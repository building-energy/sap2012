# sap2012
SAP2012 energy calculation method in Python.

## Introduction

SAP2012 is the Standard Assessment Procedure 2012, the UK Government's energy calculation method for the building regulation compliance for new dwellings. 

SAP2012 is developed and published by the Building Research Establishment: https://www.bregroup.com/sap/standard-assessment-procedure-sap-2012/.

This Python package contains the calculation methods and data in the SAP2012 methodology. It allows the user to specify the inputs needed for a SAP calculation and then to run a SAP calculation based on these inputs.

## Documentation

Full documentation is available on ReadTheDocs here: https://sap2012.readthedocs.io/en/latest/

## Installation

Available on PyPi. Download using the command `pip install sap2012`.

If using the Anaconda distribution, this command can be run using the Anaconda prompt.

## Approach

The package is designed to represent the SAP calculation method as simply as possible, to allow for flexibility and customisation. 

Each section of the SAP2012 calculation method is a separate Python function which takes the input data as a series of arguments and returns the calculation results. For example, the method for calculating ventilation rates is given in the *ventilation_rates.py* module.

A complete SAP calculation is run using the *calculate_worksheet* function.

## Quick Example

This example runs a complete SAP2012 calculation using the inputs as stored in the ['inputs.json'](https://github.com/building-energy/sap2012/blob/master/notebooks/docs/inputs.json) file. The example prints the model outputs of the 'SAP_rating' section of the calculations.

```python
from sap2012 import calculate_worksheet
import json
with open('inputs.json') as f:
    inputs=json.load(f)
result=calculate_worksheet(inputs)
print(result['SAP_rating'])
```

```
{'energy_cost_factor': 1.7754795340546146, 'SAP_rating_value': 75.23206049993813}
```

## Issues & feature requests?

Please raise them on the [GitHub Issues page](https://github.com/building-energy/sap2012/issues).

## Contributions

All contributions welcome. Please send your [pull requests](https://github.com/building-energy/sap2012/pulls).

## Contacts

https://www.lboro.ac.uk/departments/abce/staff/steven-firth/









