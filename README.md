## Project background

We manufacture customised machines using a database of thousands of frequently re-occuring parts. 
The costs of these parts increase over time due to inflation. We need a tool to inflation-correct the many material costs to be able to make accurate cost estimations for future new machines. 
## What it does

Correct (inflate) part costs in .csv or .xlsx file to the current calendar year using cumulative interest since the last known supplier quotation date. Note including current year and not including forward inflation. 

### Prerequisites

To run this project, you'll need to have the following Python packages installed:
- pandas
- datetime
- dateutil 
- openpyxl
- unittest
- os
>_note: the package name can be different from the importable name, see below_

You can install these packages using pip. 

```
pip install pandas, datetime, python-dateutil, openpyxl, unittest, os
```

You need to have your .csv or .xlsx file formatted as  'Material';'Date';'Cost'

### How to clone it

```
git clone https://github.com/zerosimon/costcorrection
```

### How to run it

```
cd costcorrection 
./tests.py
./main.py
```
---
### Constributing

If there are features that you would like to see added, feel free to add an issue here, or create a pull request implementing that feature!

### Definitions

Costs = the cost of material for manufacturing organization point of view

Price = the price of the material for supplier point of view
