This github repository contains the data and code used for paper "Small Dataset Acquisition for Machine Learning Analysis with Possible Uncertainties".

example_data:

here you can find some training data, generated with different DOE strategies. Using Minitab to get the D-optimal of a specific dataset
All the training datasets here are without uncertainty. Run the uncertainty_generation.ipynb to build datasets with uncertainties. For Emukit use emu_integratednoise.ipynb.
A test dataset with 2500 data points are give as an example. With testdata_generation.py you can generate other test datasets.


code:

relevant python scripts / jupyter notebooks for data generation, model training and others.
Python freecad API scripts for data import&export are stored in the freecad folder.
Tips:
normal.py: data normalization 
Freecad_fem.txt for building the FEM simulation in freecad with python console.
auto-sklearn.ipynb: build models with auto-sklearn

results:

Experiment results related to the paper can be found here.

requirement:

for freecad:
Python                   3.8.10
sklearn                  0.0.post5
joblib                   1.2.0
pandas                   2.0.2
numpy                    1.24.3
pyDOE                    0.3.8
pyDOE2                   1.3.0
GPy                      1.12.0

for auto-sklearn:
with WSL for linux: 
ubuntu                   22.04.1
Python                   3.10.6
auto-sklearn             0.15.0