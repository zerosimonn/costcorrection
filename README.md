Project background
To improve the quality of life for people around the world, we manufacture customized machines. While each machine configuration is unique, it is comprised of frequently re-occurring parts. The costs of these parts increase over time due to inflation. It is not possible to request up-to-date pricing to our suppliers for all parts, so 

This project aims to output a tool to estimate the current price. 

What it does
Correct material cost to current quarter based on date when quote was received. 

Prerequisites
To run this project, you'll need to have the following Python packages installed:
-
-
You can install these packages using pip. 
pip install -

How to clone it
git clone https://github.com/zerosimon/costcorrection

How to run it
cd costcorrection
./main.py

Run the tests
./test.py

Constributing
If there are features that you would like to see added, feel free to add an issue here, or create a pull request implementing that feature!

Definitions
Costs = the cost of material for manufacturing organization point of view
Price = the price of the material for supplier point of view
