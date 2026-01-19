## Project background

We configure the costs of customised manufacturing machines using a database of thousands of frequently re-occuring parts. The costs of these individual parts increase over time due to inflation. We need a tool to inflation-correct material costs to be able to make accurate cost estimations for future new machines. 
## What it does

Correct (inflate) part costs in .csv or .xlsx file to the target month of current yearm, using cumulative interest since the last known supplier quotation date. Note: including correction to month of current year but excluding forward inflation. 

### Prerequisites

To run this project, you'll need standard library modules:
- datetime
- os
- time
- unittest

... and you'll need the following third-party packages:
- pandas
- python-dateutil 
- openpyxl
>_note: the package name can be different from the importable name_

You can install 3rd party packages using pip. 

```
pip install pandas python-dateutil, openpyxl
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

### Definitions and references

Inflation data comes from [Statistics Netherlands](https://opendata.cbs.nl/#/CBS/nl/dataset/83131NED/table).

Costs = the Euro value of material from manufacturing organization point of view.

Price = the Euro value of material from supplier point of view.
