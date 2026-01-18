## Project background

To improve the quality of life for people around the world, we manufacture customized machines. While each machine configuration is unique, it is comprised of frequently re-occurring parts. The costs of these parts increase over time due to inflation. We need a tool to inflation-correct the material costs.

## What it does

Correct material cost to current quarter based on date when supplier quote was received. 
Compound interest from quote date up to (but not including) your target year. Forward inflation for current year not done.

### Prerequisites

To run this project, you'll need to have the following Python packages installed:
- pandas
- datetime
- dateutil 
- openpyxl
>(note that the package name is different from the importable name)

You can install these packages using pip. 

```pip install pandas, datetime, python-dateutil, openpyxl```

How to clone it

```git clone https://github.com/zerosimon/costcorrection```

How to run it

```
cd costcorrection 
./main.py
```

Run the tests

```./tests.py ```

---
### Constributing

If there are features that you would like to see added, feel free to add an issue here, or create a pull request implementing that feature!

### Definitions

Costs = the cost of material for manufacturing organization point of view

Price = the price of the material for supplier point of view
